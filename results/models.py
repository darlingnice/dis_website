from django.db import models

from people.models import Student
from core.models import Subject, AcademicYear

class AcademicResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)  # e.g., First Term
    score = models.DecimalField(max_digits=5, decimal_places=2)
