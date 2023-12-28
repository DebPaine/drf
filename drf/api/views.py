from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def home(request):
    """
    DRF POST API View
    """
    serializer = ProductSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        # serializer.save()
        print(data)
        return Response(data)
    # return Response({"error": "bad request"}, status=400)


# @api_view(["GET"])
# def home(request):
#     """
#     DRF GET API View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # Serialization: turning model instance into python dict (or json, etc)
#         # data = model_to_dict(model_data, fields=["id", "title"])
#         data = ProductSerializer(instance).data
#     return Response(data)


# def home(request):
#     body = (
#         request.body
#     )  # body is json byte string format, request is HTTPRequest object created by Django
#     data = json.loads(body)
#     return JsonResponse(data)


# def home(request):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # Serialization: turning model instance into python dict (or json, etc)
#         data = model_to_dict(model_data, fields=["id", "title"])
#     return JsonResponse(data)
