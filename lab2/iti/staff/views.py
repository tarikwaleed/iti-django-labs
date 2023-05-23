from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from staff.models import *


def viewList(req):
    context = {'staff': Staff.objects.all()}
    return render(req, 'staff/list_staff.html', context)


def insertStaff(req):
    if req.method == 'GET':
        return render(req, 'staff/insert_staff.html')
    else:
        Staff.objects.create(username=req.POST['username'],
                               address=req.POST['address'],
                               email=req.POST['email'],
                               password=req.POST['password'])
        return viewList(req)


def updateStaff(req, id):
    return JsonResponse({"update": "staff"})


def deleteStaff(req, id):
    return HttpResponseRedirect('/staff/list')


def getAllStaff(req):
    return Staff.objects.all()