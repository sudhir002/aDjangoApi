from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .form import Queryform
from .Querry import *


@csrf_exempt
def seLection(request):
    if request.method == "POST":
        form = Queryform(request.POST)
        inputDataid = form.data["id"]
        request = SQuerry('id', inputDataid)
        return JsonResponse(request)
    if request.method == "GET":
        data = {
            "request Type": "POST only______*",
            "info": "api information",
            "for insertdata": [{
                "api call": "/insertion",
                "input key": ["id", "real_name", "tz", "activity_periods"],
            }],
            "for selection": [{
                "api call": "/selection",
                "input key": "id"
            }]
        }
        return JsonResponse (data)
