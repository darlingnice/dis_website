from rest_framework import serializers
from .models import AcademicResult

class AcademicResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicResult
        fields = '__all__'
