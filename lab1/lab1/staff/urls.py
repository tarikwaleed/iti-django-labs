from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('',views.list_staff),
    path('insert/',views.insert_staff),
    path('update/',views.update_staff),
    path('delete/',views.delete_staff)
]