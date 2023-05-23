from django.urls import path

from . import views
from .views import *

urlpatterns=[
    path('',views.list_student),
    path('insert/',views.insert_student),
    path('update/',views.update_student),
    path('delete/',views.delete_student)
]
