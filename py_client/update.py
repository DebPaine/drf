import requests


endpoint = "http://localhost:8000/api/products/5/update/"
data = {"title": "Updated title", "content": None, "price": 499.99}
response = requests.put(endpoint, json=data)
print(response.json())
