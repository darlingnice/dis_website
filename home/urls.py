from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('classes/',views.classes,name="classes"), 
    path('facility/',views.facility,name="facility"),
    path('become-a-tearcher/',views.call_to_action,name="call-to-action"),   
    path('appointment/',views.appointment,name="appointment"), 
    path('testimonials/',views.testimonials,name="testimonials"),  
    path('contact/',views.contact,name="contact"), 
    path('parents/',views.parents,name="parents") ,
    path('admissions/',views.admissions,name="admissions")
    

]