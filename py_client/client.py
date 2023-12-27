import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"
response = requests.get(endpoint)

# .json() converts json to dict
# print(response.json())
print(response.text)
