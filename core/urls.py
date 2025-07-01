from django.urls import path
from . import views

urlpatterns = [
    path('academic-years/', views.academic_year_list_create, name='academic_year_list_create'),
    path('classes/', views.class_list_create, name='class_list_create'),
    path('sections/', views.section_list_create, name='section_list_create'),
    path('subjects/', views.subject_list_create, name='subject_list_create'),
]
