from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.utils.safestring import mark_safe
from ViewsApplications.forms import GradeForm
from Student_Account.models import *
# Create your views here.


def get_table(request):
    data = {"message": "hello world!"}
    data2 = mark_safe("<tr> Hello </tr>")
    return HttpResponse(data2)

def update_grade(request):
    if request.user.is_registrar and request.method == "POST":
        gradeObj = StudentGrade.objects.get(id = request.POST["id"])
        gradeObj.grade = request.POST["grade"]
        gradeObj.save()
        return HttpResponse("Grade has been updated")


    else:
        return HttpResponse("Permission denied")

