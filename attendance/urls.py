from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.attendance_list_create, name='attendance_list_create'),
]
