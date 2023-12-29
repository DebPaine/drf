from rest_framework import generics, mixins, permissions, authentication


from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission


# Mixins are similar to Generics but they provide more flexibility and lesser abstraction. We can combine multiple HTTP methods into a single mixin class
class ProductMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # print(self.request.user)
        content = serializer.validated_data.get("content")
        if not content:
            content = "This is a generic content"
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Detail view is for one single item, GET request
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "xyz"  # default is pk


# Create view is to add items, list view is to list items, GET and POST request
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Authentication: to validate a user and say user.is_authenticated is true
    # Permission: to see whether an authenticated user is authorized or not
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        content = serializer.validated_data.get("content")
        if not content:
            content = "wow amazing content wow"
        serializer.save(content=content)


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_destroy(self, instance):
    #     # we can do something with the instance if we want
    #     super().perform_destroy(instance)  # just does instance.delete()


# List all the objects
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
