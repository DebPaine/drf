import requests


endpoint = "http://localhost:8000/api/products/"
data = {"title": "Amazing insane title", "content": None}
response = requests.post(endpoint, json=data)
print(response.json())
