from django.forms import ModelForm 
from Student_Account.models import *


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["username", "email", 'first_name', 'last_name']

class GradeForm(ModelForm):
    class Meta:
        model = StudentGrade
        fields = ['grade']