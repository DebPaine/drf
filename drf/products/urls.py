from django.urls import path
from . import views

# by default, pk is the field lookup field
urlpatterns = [
    # using same endpoint below, we can use GET and POST request
    path("", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view()),
]
