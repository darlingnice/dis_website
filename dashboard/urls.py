from django.urls import path
from . import views



urlpatterns = [
    path('admin/',views.admin_dashboard,name="admin-dashboard"),
    path('test/',views.testing,name="admin-dashboard")
]