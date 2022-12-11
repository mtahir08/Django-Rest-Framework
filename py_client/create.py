import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "this field is done",
    "price": 34.21
}

get_response = requests.post(endpoint, json=data) # API -> Method
print(get_response.json())

