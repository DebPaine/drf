import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?")
# Ask for password in terminal without echo
password = getpass("What is your password?")
data = {"username": username, "password": password}
auth_response = requests.post(auth_endpoint, json=data)

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    print(token)
    endpoint = "http://localhost:8000/api/products/"
    response = requests.get(endpoint, headers={"Authorization": f"Bearer {token}"})
    print(response.json())
