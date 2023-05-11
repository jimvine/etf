import itertools

from etf.evaluation import utils


class EvaluationPageStatus(utils.Choices):
    DONE = "Done"
    IN_PROGRESS = "In progress"
    INCOMPLETE = "Incomplete"
    NOT_STARTED = "Not started"


page_display_names = {
    "intro": "Intro",
    "title": "Title",
    "description": "Description",
    "issue-description": "Issue description",
    "studied-population": "Studied population",
    "participant-recruitment": "Participant recruitment",
    "evaluation-costs": "Evaluation costs",
    "documents": "Documents",
    "event-dates": "Event dates",
    "evaluation-types": "Evaluation types",
    "impact-design": "Impact evaluation design",
    "impact-analysis": "Impact evaluation analysis",
    "process-design": "Process evaluation design",
    "process-analysis": "Process evaluation analysis",
    "economic-design": "Economic evaluation design",
    "economic-analysis": "Economic evaluation analysis",
    "other-design": "Other evaluation design",
    "other-analysis": "Other evaluation analysis",
    "interventions": "Interventions",
    "outcome-measures": "Outcome measures",
    "other-measures": "Other measures",
    "ethics": "Ethical considerations",
    "impact-findings": "Impact evaluation findings",
    "economic-findings": "Economic evaluation findings",
    "process-findings": "Process evaluation findings",
    "other-findings": "Other evaluation findings",
    "processes-standards": "Processes and standards",
    "grants": "Grants",
    "links": "Links and IDs",
    "visibility": "Evaluation visibility",
    "end": "End",
}

page_url_names = (
    "intro",
    "title",
    "description",
    "issue-description",
    "studied-population",
    "participant-recruitment",
    "evaluation-costs",
    "documents",
    "evaluation-types",
    "event-dates",
    "impact-design",
    "impact-analysis",
    "process-design",
    "process-analysis",
    "economic-design",
    "economic-analysis",
    "other-design",
    "other-analysis",
    "interventions",
    "outcome-measures",
    "other-measures",
    "ethics",
    "impact-findings",
    "economic-findings",
    "process-findings",
    "other-findings",
    "processes-standards",
    "grants",
    "links",
    "visibility",
    "end",
)

object_page_url_names = {
    "interventions": "intervention-page",
    "outcome-measures": "outcome-measure-page",
    "other-measures": "other-measure-page",
    "processes-standards": "processes-standard-page",
    "grants": "grant-page",
    "evaluation-costs": "evaluation-cost-page",
    "documents": "document-page",
    "links": "link-page",
    "event-dates": "event-date-page",
}

_evaluation_type_page_mapping = {
    "IMPACT": set(("impact-analysis", "impact-design", "impact-findings")),
    "PROCESS": set(("process-analysis", "process-design", "process-findings")),
    "ECONOMIC": set(("economic-analysis", "economic-design", "economic-findings")),
    "OTHER": set(("other-analysis", "other-design", "other-findings")),
}

_all_evaluation_type_pages = set().union(*_evaluation_type_page_mapping.values())


def get_prev_next_page_name(page_name, evaluation_types):
    pages = tuple(get_page_name_and_order(evaluation_types).keys())
    assert page_name in pages
    page_index = pages.index(page_name)
    if page_index == 0:
        prev_url_name = None
    else:
        prev_url_name = pages[page_index - 1]
    if page_index + 1 == len(pages):
        next_url_name = None
    else:
        next_url_name = pages[page_index + 1]
    return prev_url_name, next_url_name


default_page_statuses = {page_name: EvaluationPageStatus.NOT_STARTED.name for page_name in page_url_names}


@utils.dictify
def get_page_name_and_order(evaluation_types):
    pages_to_keep = set().union(
        *(_evaluation_type_page_mapping.get(evaluation_type, set()) for evaluation_type in evaluation_types)
    )
    pages_to_remove = _all_evaluation_type_pages - pages_to_keep
    counter = itertools.count(0)

    for page_name in page_url_names:
        if page_name not in pages_to_remove:
            yield page_name, next(counter)


def get_default_page_statuses():
    return dict(default_page_statuses)
