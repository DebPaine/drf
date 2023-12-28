from rest_framework import serializers

from .models import Product

# Serializers do a lot of things:
# 1. It is used to serialize or convert model data to python object (eg: GET)
# 2. It is used to validate if the request data is correct or not (eg: POST)
# 3. It is used for both serialization (model object to python dict) and deserialization (json request to model object)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ["title", "content", "price", "sale_price", "discount"]
        fields = "__all__"
        # exclude = ["content"]
