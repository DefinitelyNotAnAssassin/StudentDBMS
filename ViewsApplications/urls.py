from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path("information", views.student_information, name = "student information"),
    path("registrar", views.regisrar_module, name = "registrar module"),
    path("student/<str:section>/<int:student_id>", views.search_result, name = "search result"),
    path("subject/edit_grade/<int:id>", views.edit_grade, name = "edit grade" )
    

]