from django.urls import path
from . import views



urlpatterns = [
    path('admin/',views.admin_dashboard,name="admin-dashboard"),
    path('register/student/',views.add_student,name="add_student")
]