import requests


endpoint = "http://localhost:8000/api/products/3/update/"
data = {"title": "Updated title", "content": None}
response = requests.put(endpoint, json=data)
print(response.json())
