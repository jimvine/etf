import marshmallow
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from . import choices, interface, models, pages, schemas
from .utils import check_edit_evaluation_permission


@login_required
def index_view(request):
    return render(request, "index.html")


def make_evaluation_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse(page_name, args=(evaluation_id,))


@login_required
def create_evaluation(request):
    if request.method == "POST":
        title = request.POST.get("title")
        short_title = request.POST.get("short_title")
        user = request.user
        evaluation_data = interface.facade.evaluation.create(user_id=user.id)
        evaluation_data = interface.facade.evaluation.update(
            user_id=user.id, evaluation_id=evaluation_data["id"], data={"title": title, "short_title": short_title}
        )
        evaluation_id = evaluation_data["id"]
        return redirect(
            intro_page_view,
            evaluation_id=evaluation_id,
        )
    else:
        return render(request, "submissions/create.html", {"title": "Create evaluation", "errors": {}, "data": {}})


@login_required
@check_edit_evaluation_permission
def simple_page_view(request, evaluation_id, page_data):
    page_name = page_data["page_name"]
    user = request.user
    evaluation = interface.facade.evaluation.get(user.id, evaluation_id)
    prev_url_name, next_url_name = pages.get_prev_next_page_name(page_name, evaluation["evaluation_type"])
    prev_url = make_evaluation_url(evaluation_id, prev_url_name)
    next_url = make_evaluation_url(evaluation_id, next_url_name)
    page_name = page_data["page_name"]
    template_name = f"submissions/{page_name}.html"
    title = page_data["title"]
    page_statuses = evaluation["page_statuses"]
    form_data = {
        "title": title,
        "prev_url": prev_url,
        "next_url": next_url,
        "evaluation_id": evaluation_id,
        "page_statuses": page_statuses,
        "page_order": pages.get_page_name_and_order(evaluation["evaluation_type"]),
        "current_page": page_name,
    }
    interface.facade.evaluation.update_page_status(
        user.id, evaluation_id, page_name, models.EvaluationPageStatus.DONE.name
    )
    return render(request, template_name, form_data)


def transform_post_data(post_data, multiselect_dropdown_choices):
    """
    Keep lists of variables from request.POST for multiselect fields.
    """
    data = post_data.dict()
    for var_name in multiselect_dropdown_choices:
        if var_name in post_data:
            data[var_name] = post_data.getlist(var_name)
    return data


@login_required
@check_edit_evaluation_permission
def evaluation_view(request, evaluation_id, page_name, title):
    user = request.user
    evaluation = interface.facade.evaluation.get(user.id, evaluation_id)
    prev_url_name, next_url_name = pages.get_prev_next_page_name(page_name, evaluation["evaluation_type"])
    next_url = make_evaluation_url(evaluation_id, next_url_name)
    prev_url = make_evaluation_url(evaluation_id, prev_url_name)
    template_name = f"submissions/{page_name}.html"
    evaluation_schema = schemas.EvaluationSchema(unknown=marshmallow.EXCLUDE)
    errors = {}
    statuses = choices.EvaluationStatus.choices
    page_statuses = evaluation["page_statuses"]
    multiple_value_vars = ["topics", "organisations", "evaluation_type", "impact_design_name"]
    if request.GET.get("completed"):
        interface.facade.evaluation.update_page_status(
            user.id, evaluation_id, page_name, models.EvaluationPageStatus.DONE.name
        )
    if request.method == "POST":
        data = transform_post_data(request.POST, multiple_value_vars)
        try:
            serialized_evaluation = evaluation_schema.load(data=data, partial=True)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
        else:
            interface.facade.evaluation.update(user.id, evaluation_id, serialized_evaluation)
            interface.facade.evaluation.update_page_status(
                user.id, evaluation_id, page_name, models.EvaluationPageStatus.DONE.name
            )
            return redirect(next_url)

    else:
        interface.facade.evaluation.update_page_status(
            user.id, evaluation_id, page_name, models.EvaluationPageStatus.IN_PROGRESS.name
        )
        data = evaluation
    return render(
        request,
        template_name,
        {
            "errors": errors,
            "dropdown_choices": choices.dropdown_choices,
            "statuses": statuses,
            "data": data,
            "next_url": next_url,
            "prev_url": prev_url,
            "title": title,
            "page_order": pages.get_page_name_and_order(evaluation["evaluation_type"]),
            "current_page": page_name,
            "evaluation_id": evaluation_id,
            "page_statuses": page_statuses,
            "object_name": page_name,
        },
    )


def add_related_object_for_evaluation(evaluation_id, model_name, redirect_url_name, object_name=""):
    model = getattr(models, model_name)
    new_object = model(evaluation_id=evaluation_id)
    if object_name:
        new_object.set_name(f"New {object_name}")
    new_object.save()
    response = redirect(reverse(redirect_url_name, args=(evaluation_id,)))

    return response


def get_related_object_page_url_names(summary_page_name, evaluation_type):
    prev_section_url_name, next_section_url_name = pages.get_prev_next_page_name(summary_page_name, evaluation_type)
    url_names = {
        "page": pages.object_page_url_names[summary_page_name],
        "prev_section_url_name": prev_section_url_name,
        "next_section_url_name": next_section_url_name,
        "summary_page": summary_page_name,
    }
    return url_names


def make_summary_related_object_context(evaluation, model_name, form_data):
    evaluation_id = evaluation["id"]
    data = {"evaluation_id": evaluation_id}
    title = form_data["title"]
    page_statuses = evaluation["page_statuses"]
    object_name = form_data["object_name"]
    object_name_plural = form_data["object_name_plural"]
    summary_page_name = form_data["summary_page_name"]
    object_page_name = pages.object_page_url_names[summary_page_name]
    url_names = get_related_object_page_url_names(summary_page_name, evaluation["evaluation_type"])
    prev_url_name = url_names["prev_section_url_name"]
    next_url_name = url_names["next_section_url_name"]
    prev_url = reverse(prev_url_name, args=(evaluation_id,))
    next_url = reverse(next_url_name, args=(evaluation_id,))
    page_statuses = evaluation["page_statuses"]
    errors = {}
    related_model = getattr(models, model_name)
    all_objects = related_model.objects.filter(evaluation__id=evaluation_id)
    data["objects_url_mapping"] = {
        reverse(object_page_name, args=(evaluation_id, obj.id)): obj.get_name() for obj in all_objects
    }
    data["object_name"] = object_name
    data["object_name_plural"] = object_name_plural
    data["object_summary_page_name"] = summary_page_name
    return {
        "title": title,
        "errors": errors,
        "data": data,
        "prev_url": prev_url,
        "next_url": next_url,
        "page_order": pages.get_page_name_and_order(evaluation["evaluation_type"]),
        "current_page": summary_page_name,
        "evaluation_id": evaluation_id,
        "page_statuses": page_statuses,
    }


@login_required
@check_edit_evaluation_permission
def summary_related_object_page_view(request, evaluation_id, model_name, form_data):
    user = request.user
    evaluation = interface.facade.evaluation.get(user.id, evaluation_id)
    object_name = form_data["object_name"]
    summary_page_name = form_data["summary_page_name"]

    if request.GET.get("completed"):
        completed_page_name = request.GET.get("completed")
        interface.facade.evaluation.update_page_status(
            user.id, evaluation_id, completed_page_name, models.EvaluationPageStatus.DONE.name
        )

    if request.method == "POST":
        # TODO - figure out logic for evaluation status
        return add_related_object_for_evaluation(
            evaluation_id=evaluation_id,
            model_name=model_name,
            redirect_url_name=summary_page_name,
            object_name=object_name,
        )
    else:
        template_name = form_data["template_name"]
        interface.facade.evaluation.update_page_status(
            user.id, evaluation_id, summary_page_name, models.EvaluationPageStatus.IN_PROGRESS.name
        )
        context = make_summary_related_object_context(evaluation, model_name, form_data)
        response = render(request, template_name, context)
    return response


def make_related_object_context(user_id, evaluation_id, title, object_name, url_names):
    evaluation = interface.facade.evaluation.get(user_id, evaluation_id)
    next_url = reverse(url_names["next_section_url_name"], args=(evaluation_id,))
    prev_url = reverse(url_names["prev_section_url_name"], args=(evaluation_id,))
    summary_url = reverse(url_names["summary_page"], args=(evaluation_id,))
    page_statuses = evaluation["page_statuses"]
    url_names = get_related_object_page_url_names(url_names["summary_page"], evaluation["evaluation_type"])
    return {
        "title": title,
        "next_url": next_url,
        "prev_url": prev_url,
        "object_name": object_name,
        "summary_url": summary_url,
        "page_order": pages.get_page_name_and_order(evaluation["evaluation_type"]),
        "current_page": url_names["summary_page"],
        "evaluation_id": evaluation_id,
        "page_statuses": page_statuses,
        "dropdown_choices": choices.dropdown_choices,
    }


@login_required
@check_edit_evaluation_permission
def related_object_page_view(request, evaluation_id, id, model_name, title, template_name, url_names):
    model = getattr(models, model_name)
    schema = getattr(schemas, f"{model_name}Schema")
    obj = model.objects.get(id=id)
    errors = {}
    model_schema = schema(unknown=marshmallow.EXCLUDE)
    next_url = reverse(url_names["next_section_url_name"], args=(evaluation_id,))
    summary_url = reverse(url_names["summary_page"], args=(evaluation_id,))
    multiple_value_vars = ["document_types"]
    if request.method == "POST":
        data = transform_post_data(request.POST, multiple_value_vars)
        if "delete" in request.POST:
            obj.delete()
            return redirect(summary_url)
        try:
            serialized_obj = model_schema.load(data=data, partial=True)
            for field_name in serialized_obj:
                setattr(obj, field_name, serialized_obj[field_name])
            obj.save()
            if "return" in request.POST:
                return redirect(summary_url)
            return redirect(next_url)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
    else:
        data = model_schema.dump(obj)
    context = make_related_object_context(request.user.id, evaluation_id, title, template_name, url_names)
    context = {"errors": errors, "data": data, **context}
    return render(request, template_name, context)


def intro_page_view(request, evaluation_id):
    page_data = {"title": "Introduction", "page_name": "intro"}
    return simple_page_view(request, page_data=page_data, evaluation_id=evaluation_id)


def evaluation_title_view(request, evaluation_id):
    page_data = {"title": "Title", "page_name": "title"}
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_description_view(request, evaluation_id):
    page_data = {
        "title": "Description",
        "page_name": "description",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_issue_description_view(request, evaluation_id):
    page_data = {
        "title": "Issue description",
        "page_name": "issue-description",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_studied_population_view(request, evaluation_id):
    page_data = {
        "title": "Studied population",
        "page_name": "studied-population",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_participant_recruitment(request, evaluation_id):
    page_data = {
        "title": "Participant recruitment",
        "page_name": "participant-recruitment",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_costs_view(request, evaluation_id):
    page_data = {
        "title": "Evaluation costs and budget",
        "page_name": "evaluation-costs",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_policy_costs_view(request, evaluation_id):
    page_data = {
        "title": "Policy costs and budget",
        "page_name": "policy-costs",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_publication_intention_view(request, evaluation_id):
    page_data = {
        "title": "Publication intention",
        "page_name": "publication-intention",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_types_view(request, evaluation_id):
    page_data = {
        "title": "Evaluation types",
        "page_name": "evaluation-types",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_impact_design_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation design",
        "page_name": "impact-design",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_impact_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation analysis",
        "page_name": "impact-analysis",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_process_design_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation design",
        "page_name": "process-design",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_process_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation analysis",
        "page_name": "process-analysis",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_economic_design_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation design",
        "page_name": "economic-design",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_economic_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation analysis",
        "page_name": "economic-analysis",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_other_design_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation design",
        "page_name": "other-design",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_other_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation analysis",
        "page_name": "other-analysis",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_ethics_view(request, evaluation_id):
    page_data = {
        "title": "Ethical considerations",
        "page_name": "ethics",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_impact_findings_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation findings",
        "page_name": "impact-findings",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_economic_findings_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation findings",
        "page_name": "economic-findings",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_process_findings_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation findings",
        "page_name": "process-findings",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_other_findings_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation findings",
        "page_name": "other-findings",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_metadata_view(request, evaluation_id):
    page_data = {
        "title": "Metadata",
        "page_name": "metadata",
    }
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def evaluation_status_view(request, evaluation_id):
    page_data = {"title": "Evaluation status", "page_name": "status"}
    return evaluation_view(request, evaluation_id=evaluation_id, **page_data)


def end_page_view(request, evaluation_id):
    page_data = {"title": "End", "page_name": "end"}
    return simple_page_view(request, page_data=page_data, evaluation_id=evaluation_id)


def summary_interventions_page_view(request, evaluation_id):
    form_data = {
        "title": "Interventions",
        "template_name": "submissions/interventions.html",
        "prev_section_url_name": "other-analysis",
        "next_section_url_name": "outcome-measures",
        "page_url_name": "intervention-page",
        "summary_page_name": "interventions",
        "object_name": "intervention",
        "object_name_plural": "interventions",
    }
    model_name = "Intervention"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def intervention_page_view(request, evaluation_id, intervention_id):
    model_name = "Intervention"
    title = "Interventions"
    template_name = "submissions/intervention-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("interventions", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=intervention_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_outcome_measure_page_view(request, evaluation_id):
    form_data = {
        "title": "Outcome measures",
        "template_name": "submissions/outcome-measures.html",
        "summary_page_name": "outcome-measures",
        "object_name": "outcome measure",
        "object_name_plural": "outcome measures",
    }
    model_name = "OutcomeMeasure"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    model_name = "OutcomeMeasure"
    title = "Outcome measures"
    template_name = "submissions/outcome-measure-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("outcome-measures", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=outcome_measure_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_other_measure_page_view(request, evaluation_id):
    form_data = {
        "title": "Other measures",
        "template_name": "submissions/other-measures.html",
        "summary_page_name": "other-measures",
        "object_name": "other measure",
        "object_name_plural": "other measures",
    }
    model_name = "OtherMeasure"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def other_measure_page_view(request, evaluation_id, other_measure_id):
    model_name = "OtherMeasure"
    title = "Other measures"
    template_name = "submissions/other-measure-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("other-measures", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=other_measure_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_processes_standards_page_view(request, evaluation_id):
    form_data = {
        "title": "Processes and standards",
        "template_name": "submissions/processes-standards.html",
        "summary_page_name": "processes-standards",
        "object_name": "process or standard",
        "object_name_plural": "processes and standards",
    }
    model_name = "ProcessStandard"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def process_standard_page_view(request, evaluation_id, process_standard_id):
    model_name = "ProcessStandard"
    title = "Processes and standards"
    template_name = "submissions/processes-standard-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("processes-standards", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=process_standard_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_grants_page_view(request, evaluation_id):
    form_data = {
        "title": "Grants",
        "template_name": "submissions/grants.html",
        "summary_page_name": "grants",
        "object_name": "grant",
        "object_name_plural": "grants",
    }
    model_name = "Grant"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def grant_page_view(request, evaluation_id, grant_id):
    model_name = "Grant"
    title = "Grant"
    template_name = "submissions/grant-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("grants", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=grant_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_evaluation_costs_page_view(request, evaluation_id):
    form_data = {
        "title": "Evaluation costs and budget",
        "template_name": "submissions/evaluation-costs.html",
        "summary_page_name": "evaluation-costs",
        "object_name": "evaluation cost",
        "object_name_plural": "evaluation costs",
    }
    model_name = "EvaluationCost"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def evaluation_cost_page_view(request, evaluation_id, evaluation_cost_id):
    model_name = "EvaluationCost"
    title = "Evaluation costs and budget"
    template_name = "submissions/evaluation-cost-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("evaluation-costs", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=evaluation_cost_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def evaluation_overview_view(request, evaluation_id):
    user = request.user
    evaluation = interface.facade.evaluation.get(user.id, evaluation_id)
    statuses = evaluation["page_statuses"]
    data = {
        "statuses": statuses,
        "page_order": pages.get_page_name_and_order(evaluation["evaluation_type"]),
        "evaluation_id": evaluation_id,
    }
    errors = {}
    return render(request, "submissions/overview.html", {"errors": errors, "data": data})


def summary_documents_page_view(request, evaluation_id):
    form_data = {
        "title": "Documents",
        "template_name": "submissions/documents.html",
        "summary_page_name": "documents",
        "object_name": "document",
        "object_name_plural": "documents",
    }
    model_name = "Document"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def document_page_view(request, evaluation_id, document_id):
    model_name = "Document"
    title = "Document"
    template_name = "submissions/document-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("documents", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=document_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_links_page_view(request, evaluation_id):
    form_data = {
        "title": "Links to other services",
        "template_name": "submissions/links.html",
        "summary_page_name": "links",
        "object_name": "link",
        "object_name_plural": "links",
    }
    model_name = "LinkOtherService"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def links_page_view(request, evaluation_id, link_id):
    model_name = "LinkOtherService"
    title = "Links to other service"
    template_name = "submissions/links-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("links", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=link_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response


def summary_event_dates_page_view(request, evaluation_id):
    form_data = {
        "title": "Event dates",
        "template_name": "submissions/event-dates.html",
        "summary_page_name": "event-dates",
        "object_name": "event date",
        "object_name_plural": "event dates",
    }
    model_name = "EventDate"
    return summary_related_object_page_view(
        request, model_name=model_name, form_data=form_data, evaluation_id=evaluation_id
    )


def event_date_page_view(request, evaluation_id, event_date_id):
    model_name = "EventDate"
    title = "Event date"
    template_name = "submissions/event-date-page.html"
    evaluation = interface.facade.evaluation.get(request.user.id, evaluation_id)
    url_names = get_related_object_page_url_names("event-dates", evaluation["evaluation_type"])
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=event_date_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        url_names=url_names,
    )
    return response
