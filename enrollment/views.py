from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment
from .serializers import EnrollmentSerializer

@api_view(['GET', 'POST'])
def enrollment_list_create(request):
    if request.method == 'GET':
        queryset = Enrollment.objects.all()
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
