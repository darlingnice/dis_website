from django.db import models

class AcademicYear(models.Model):
    year = models.CharField(max_length=9, unique=True)
    is_current = models.BooleanField(default=False)

class SchoolClass(models.Model):
    name = models.CharField(max_length=50)

class Section(models.Model):
    name = models.CharField(max_length=50)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

