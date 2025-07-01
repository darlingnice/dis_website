from django.db import models

from core.models import AcademicYear, SchoolClass, Section
from people.models import Student

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)
    date_enrolled = models.DateField(auto_now_add=True)
