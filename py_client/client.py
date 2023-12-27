import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
# params={"abc": 123} is for query string, eg: http://localhost:8000/api/?abc=123
response = requests.get(
    endpoint, params={"abc": 123}, json={"body": "some random request body"}
)
# .json() converts json to dict
print(response.json())
# print(response.text)
