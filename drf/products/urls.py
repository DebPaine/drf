from django.urls import path
from . import views

# by default, pk is the field lookup field
urlpatterns = [
    path("", views.ProductMixinView.as_view()),  # list
    path("<int:pk>/", views.ProductMixinView.as_view()),  # retrieve
    path("<int:pk>/update/", views.ProductMixinView.as_view()),
    path("<int:pk>/delete/", views.ProductMixinView.as_view()),
]
