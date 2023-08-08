from django.urls import path
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.school_list, name='school_list'),
]
