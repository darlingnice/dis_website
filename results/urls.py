from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.result_list_create, name='result_list_create'),
]
