from django.shortcuts import render

import student.views
from staff.models import *
from student.models import *
from student.views import *

# Create your views here.


def registerForm(req):
    if req.method == 'GET':
        context = {'staff': Staff.objects.all()}
        return render(req, 'register/register.html', context)
    else:
        return student.views.insertStudent(req)