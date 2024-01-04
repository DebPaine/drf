from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


# ModelViewset already has all the list, retrieve, create, etc, mixins inherited, check the definition for ModelViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Viewset with only Retrieve and List actions allowed
class ProductRetrieveCreateViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    # mixins.ListModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
