from rest_framework import serializers
from .models import Guardian, Student

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    guardian = GuardianSerializer(read_only=True)
    guardian_id = serializers.PrimaryKeyRelatedField(
        queryset=Guardian.objects.all(),
        source='guardian',
        write_only=True
    )

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'date_of_birth', 'gender', 'admission_number',
                  'guardian', 'guardian_id', 'address', 'date_admitted', 'active']
