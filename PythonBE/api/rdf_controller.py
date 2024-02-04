import json

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from api.rdf_service import insert, get_data, get_specific_data, get_filtered_data


@api_view(['GET'])
def hello(request):
    response = {'hello': 'user'}
    return JsonResponse(response)
    # return HttpResponse(status=200)


@api_view(['POST'])
def insert_esolang(request):
    body = json.loads(request.body)
    insert(body)
    return HttpResponse(status=200)


@api_view(['POST'])
def get_rdf_data(request):
    try:
        key = request.GET.get('key')
        if key == "esolangs_labels":
            try:
                body = json.loads(request.body)
                if len(body.keys()) != 0:
                    data = get_filtered_data(body)
                    return JsonResponse(data, safe=False)
                else:
                    return JsonResponse([], safe=False)
            except Exception as e:
                print(str(e))
                data = get_data(key)
                return JsonResponse(data, safe=False)
            # finally:
            #     data = get_data(key)
            #     return JsonResponse(data, safe=False)
        else:
            data = get_data(key)
            return JsonResponse(data, safe=False)
    except KeyError as _:
        return HttpResponse(status=400, content="Invalid key")
    # except Exception as e:
    #     return HttpResponse(status=500, content=str(e))


@api_view(['GET'])
def get_rdf_specific_data(request):
    try:
        key = request.GET.get('key')
        value = request.GET.get('value')
        data = get_specific_data(key, value)
        return JsonResponse(data, safe=False)
    except KeyError as _:
        return HttpResponse(status=400, content="Invalid key")
    # except Exception as e:
    #     return HttpResponse(status=500, content=str(e))
