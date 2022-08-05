from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path("information", views.student_information, name = "student information"),
    path("registrar", views.regisrar_module, name = "registrar module"),
    path("/student/<slug:section>/<int:student_id>", views.search_result, name = "search result"),
    

]