from django.urls import path
from . import views

urlpatterns = [
    path('guardians/', views.guardian_list_create, name='guardian_list_create'),
    path('students/', views.student_list_create, name='student_list_create'),
]
