import os
from django.shortcuts import render
from django.http import JsonResponse

path = os.getcwd()
filepath = path+"/file"
def welcome(request):
    data = {
        "info": "api information",
        "for insertdata": [{
            "api call": "/insertion",
            "input key": ["id", "real_name", "tz", "activity_periods"],
        }],
        "for selection": [{
            "api call": "/selection",
            "input key" : "id"
        }],
        "path": os.listdir(filepath)
    }
    return JsonResponse (data)

