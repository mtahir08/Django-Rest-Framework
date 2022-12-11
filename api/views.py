import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HTTPRequest -> Django
    print(request.GET)
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    # data['headers'] = request.headers # request.META
    return JsonResponse({ "message" : "HI THERE: this is your Django API response"})