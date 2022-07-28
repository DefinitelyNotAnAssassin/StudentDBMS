from Student_Account.models import *
import django_tables2 as tables

class StudentTable(tables.Table):
    class Meta:
        model = StudentProfile
        fields = ['user__first_name', 'section']