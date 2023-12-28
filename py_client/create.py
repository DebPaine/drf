import requests


endpoint = "http://localhost:8000/api/products/"
data = {"title": "Amazing insane title", "content": "some random content"}
response = requests.post(endpoint, json=data)
print(response.json())
