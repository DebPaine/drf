from django.urls import path
from . import views

# by default, pk is the field lookup field
urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),  # list
    path("<int:pk>/", views.ProductMixinView.as_view()),  # retrieve
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view()),
]
