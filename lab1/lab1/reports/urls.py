from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('liststudent/',views.student_report),
    path('liststaff/',views.staff_report),
    path('mainreport/',views.main_report)
]

