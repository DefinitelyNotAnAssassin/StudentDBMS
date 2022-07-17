from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.


def get_table(request):
    data = {"message": "hello world!"}

    return JsonResponse(data)