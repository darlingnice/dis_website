from django.db import models

from people.models import Student
from core.models import AcademicYear

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
