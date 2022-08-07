from tokenize import Single
from traceback import format_list
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from Student_Account.models import Account, StudentProfile, Class_Section, SubjectTeacher
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from ViewsApplications.forms import AccountForm, GradeForm
from django.views.generic import ListView
from ViewsApplications.filters import *
from .tables import StudentTable
from django_tables2 import SingleTableView
# Create your views here.



def index(request):
    items = {
        "form": AuthenticationForm()
    }
    return render(request, "ViewsApplications/index.html", context = items)

def login(request):
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user = authenticate(request, username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password"))
        auth_login(request, user)
        if not user.is_registrar:
          url = redirect("student information")
        elif user.is_registrar:
            url = redirect("registrar module")
        return url
    else:
        return HttpResponse("Invalid User")

@login_required
def student_information(request):

    items = {
        "user" : request.user.student,
        'subjects': request.user.student.grade.all()
    }

    return render(request, "ViewsApplications/information.html", context = items)




@login_required
def regisrar_module(request):
    if request.user.is_registrar:
        form = AccountForm()
        filtr = StudentAccountFilter(request.GET)
        table = StudentTable(filtr.qs)
        items = {
            "form": form,
            "filter": filtr,
            "table": table
        }
    
        return render(request, "ViewsApplications/registrar_module.html", context = items)
    else:
        return HttpResponse("You are not allowed here")
        
@login_required
def search_result(request, section, student_id):
  if request.user.is_registrar:
    student = get_object_or_404(StudentProfile.objects.filter(user = student_id))
    items = {
      "user" : student,
      "subjects": student.grade.all()
    }
      
    return render(request, "ViewsApplications/edit_student.html", context = items)
  else:
    return HttpResponse('Not allowed.')

@login_required
def edit_grade(request, id):
    if request.user.is_registrar:
        gradeObj = StudentGrade.objects.get(id = id)
        print(gradeObj)
        form = GradeForm(instance=gradeObj)
        items = {

            "grade": gradeObj,
            "form": form


        }
        return render(request, "ViewsApplications/edit_grade.html", context = items)
    else:
        return HttpResponse("You are not allowed here.")
