from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm

from Student_Account.models import Account, TeacherProfile, Subject, Class_Section, SubjectTeacher, StudentProfile, StudentGrade
class AccountAdmin(UserAdmin):
    list_display = ( "first_name", "id_number", "last_name","date_joined","last_login", "is_staff", "is_active", "is_superuser", "is_registrar", "is_student", "is_teacher")
    search_fields = ["id_number"]
    readonly_fields = ["date_joined", "last_login"]
    ordering = ("id_number",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
    filter_horizontal = ("teacher", )



class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = ['subject', 'teacher', 'semester']
    filter_horizontal = ("students",)







admin.site.register(Account, AccountAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Class_Section )
admin.site.register(SubjectTeacher, SubjectTeacherAdmin)
admin.site.register(StudentProfile)
admin.site.register(StudentGrade)