from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def list_staff(req):
    return HttpResponse("list staff")

def insert_staff(req):
    return JsonResponse({'status':'success','message':'staff inerted successufully'})


def update_staff(req):
    return JsonResponse({'status':'success','message':'staff updated successufully'})

def delete_staff(req):
    return HttpResponse('Staff Deleted. Redirect to Staff List')

