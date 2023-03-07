import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from flatten_json import flatten

from etf.evaluation.models import Evaluation, EvaluationStatus
from etf.evaluation.schemas import EvaluationSchema


def filter_evaluations_to_download(request):
    output_evaluations_qs = Evaluation.objects.none()
    if "civil_service_only" in request.GET:
        civil_service_evals = Evaluation.objects.filter(status=EvaluationStatus.CIVIL_SERVICE)
        output_evaluations_qs = output_evaluations_qs | civil_service_evals
    if "public" in request.GET:
        public_evals = Evaluation.objects.filter(status=EvaluationStatus.PUBLIC)
        output_evaluations_qs = output_evaluations_qs | public_evals
    if "my_evaluations" in request.GET:
        user = request.user
        user_evals = user.evaluations.all()
        output_evaluations_qs = output_evaluations_qs | user_evals
    return output_evaluations_qs


@login_required
def download_json_view(request):
    evaluations_qs = filter_evaluations_to_download(request)
    evaluation_schema = EvaluationSchema()
    data = evaluation_schema.dumps(evaluations_qs, many=True)
    headers = {
        "Content-Type": "application/json",
        "Content-Disposition": "attachment; filename=evaluation-data.json",
    }
    response = HttpResponse(data, headers=headers)
    return response


@login_required
def download_csv_view(request):
    evaluations_qs = filter_evaluations_to_download(request)
    evaluation_schema = EvaluationSchema()
    data = evaluation_schema.dump(evaluations_qs, many=True)
    flattened_dict = [flatten(d) for d in data]
    # TODO - this doesn't get data in the format that we want it
    # Also need headers for rows
    headers = {
        "Content-Type": "text/csv",
        "Content-Disposition": "attachment; filename=evaluation-data.csv",
    }
    response = HttpResponse(headers=headers)
    writer = csv.writer(response)
    for row in flattened_dict:
        writer.writerow(row)
    return response


@login_required
def download_page_view(request):
    if "json" in request.GET:
        return redirect(reverse("data-download-json"))
    elif "csv" in request.GET:
        return redirect(reverse("data-download-json"))
    return render(request, "data-download.html", {"errors": {}, "data": {}})
