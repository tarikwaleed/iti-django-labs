from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_report(req):
    return HttpResponse('student report')

def staff_report(req):
    return HttpResponse('<h1>staff kkk report</h1>')

def main_report(req):
    return HttpResponse('<a href="{% url liststaff %}">mainreport</a>')