from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Go to /auth route and obtain the token directly for the user
urlpatterns = [path("auth/", obtain_auth_token), path("", views.home, name="home")]
