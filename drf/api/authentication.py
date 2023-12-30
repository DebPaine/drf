from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class CustomTokenAuth(TokenAuthentication):
    # Replace "Token" with "Bearer", can use any keyword of our choice
    keyword = "Bearer"
