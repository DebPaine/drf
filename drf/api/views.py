from django.http import JsonResponse
import json


def home(request):
    body = (
        request.body
    )  # body is json byte string format, request is HTTPRequest object created by Django
    data = json.loads(body)
    return JsonResponse(data)
