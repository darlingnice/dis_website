from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Guardian, Student
from .serializers import GuardianSerializer, StudentSerializer

@api_view(['GET', 'POST'])
def guardian_list_create(request):
    if request.method == 'GET':
        queryset = Guardian.objects.all()
        serializer = GuardianSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = GuardianSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
