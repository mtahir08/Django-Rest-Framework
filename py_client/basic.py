import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.post(endpoint, json={"title":"abc","content":"this is item"}) # API -> Method
# print(get_response.text)


print(get_response.json())

