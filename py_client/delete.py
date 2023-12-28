import requests

id = input("What is the product id that you want to delete?")

try:
    id = int(id)
except Exception as e:
    print(e)

endpoint = f"http://localhost:8000/api/products/{id}/delete/"
response = requests.delete(endpoint)
print(response.text)
