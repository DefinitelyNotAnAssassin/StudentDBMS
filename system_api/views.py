from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.utils.safestring import mark_safe
# Create your views here.


def get_table(request):
    data = {"message": "hello world!"}
    data2 = mark_safe("<tr> Hello </tr>")
    return HttpResponse(data2)

