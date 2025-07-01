from django.db import models

class Guardian(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_number = models.CharField(max_length=30, unique=True)
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True, related_name='students')
    address = models.TextField(blank=True)
    date_admitted = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
