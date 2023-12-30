from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

"""
Steps:
1. The user first logs in using username and password
2. A token is generated and stored in DB if it's not already there for the user.
3. Using this token, the user can make requests that they are authorized to make.
4. Note: Even if the user has a token but they are not explicitly authorized to view, add, delete, change, etc, they still won't have access.
"""


class CustomTokenAuth(TokenAuthentication):
    # Replace "Token" with "Bearer", can use any keyword of our choice
    keyword = "Bearer"
