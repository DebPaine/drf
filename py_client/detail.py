import requests

id = input("Enter the product id that you want info about")

try:
    int(id)
except Exception as e:
    print(e)

endpoint = f"http://localhost:8000/api/products/{id}/"
response = requests.get(endpoint)
print(response.json())
