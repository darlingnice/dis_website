from django.shortcuts import render


def admin_dashboard(request):
    return render(request,"admin_dashboard.html",{})



def add_student(request):
    return render(request,"add_student.html",{})