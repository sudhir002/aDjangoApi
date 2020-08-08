from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .form import Queryform
from .Querry import *


@csrf_exempt
def inSertion(request):
    if request.method == "POST":
        form = Queryform(request.POST)
        id = form.data["id"]
        real_name = form.data["real_name"]
        tz = form.data["tz"]
        start_time = form.data["start_time"]
        end_time = form.data["end_time"]
        if id and real_name and tz and start_time and end_time:
            request = Querry(id, real_name, tz, start_time, end_time)
        else:
            return JsonResponse({"Status": "Failed", "Reson":"Please enter all required values__"})
        return  JsonResponse (request)

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
