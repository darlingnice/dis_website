from django.shortcuts import render


def home(request):
    return render(request,"home.html",{})



def about(request):
    return render(request,"about.html",{})

def classes(request):
    return render(request,"classes.html",{})


def facility(request):
    return render(request,"facility.html",{})


def call_to_action(request):
    return render(request,"call-to-action.html",{})

def appointment(request):
    return render(request,"appointment.html",{})

def testimonials(request):
    return render(request,"testimonials.html",{})


def contact(request):
    return render(request,"contact.html",{})