from django.urls import path 
from . import views

urlpatterns = [ 

    path("get_table", views.get_table, name = "get table" ),
    path("edit_grade", views.update_grade, name = "update grade")
]