from django.shortcuts import render


def admin_dashboard(request):
    return render(request,"admin_dashboard.html",{})


def testing(request):
    return render(request,"test.html",{})