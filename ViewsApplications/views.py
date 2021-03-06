from traceback import format_list
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Student_Account.models import Account, StudentProfile, Class_Section, SubjectTeacher
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from ViewsApplications.forms import AccountForm
from django.views.generic import ListView

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
        url = redirect("student information")
        return url
    else:
        return HttpResponse("Invalid User")

@login_required
def student_information(request):

    items = {
        "user" : request.user,
        'subjects': request.user.student.grade.all()
    }

    return render(request, "ViewsApplications/information.html", context = items)




@login_required
def regisrar_module(request):
    if request.user.is_registrar:
        form = AccountForm()
        data = SubjectTeacher.objects.all()
        print(data.values())
        items = {
            "form": form,
            'data': data
        }
        return render(request, "ViewsApplications/registrar_module.html", context = items)
    else:
        return HttpResponse("You are not allowed here")