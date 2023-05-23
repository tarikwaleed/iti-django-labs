from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def list_student(req):
    return HttpResponse("list students")

def insert_student(req):
    return render(req,'student/insert.html')

def update_student(req):
    return render(req,'student/update.html')

def delete_student(req):
    # redirect('student_list')
    return HttpResponse('Student Deleted. Redirect to Student List')
