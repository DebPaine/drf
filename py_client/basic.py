import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
# params={"abc": 123} is for query string, eg: http://localhost:8000/api/?abc=123
response = requests.post(
    endpoint, json={"title": None, "content": "some random content"}
)
# .json() converts json to dict
print(response.json())
# print(response.text)
