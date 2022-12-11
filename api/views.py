import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HTTPRequest -> Django
    # print(request.GET)
    # print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    # data['headers'] = request.headers # request.META
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    # data['content_type'] = dict(request.content_type)

    return JsonResponse(data)