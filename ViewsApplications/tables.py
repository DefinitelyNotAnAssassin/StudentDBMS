from Student_Account.models import *
import django_tables2 as tables

class StudentTable(tables.Table):
    class Meta:
        model = StudentProfile
        template_name = "ViewsApplications/registrar_module.html"
        fields = ['user__id_number', 'user__first_name','user__last_name', 'section']
        
        
        
