from django.urls import path
from . import views

urlpatterns = [
    path('enrollments/', views.enrollment_list_create, name='enrollment_list_create'),
]
