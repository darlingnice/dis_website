from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AcademicResult
from .serializers import AcademicResultSerializer

@api_view(['GET', 'POST'])
def result_list_create(request):
    if request.method == 'GET':
        queryset = AcademicResult.objects.all()
        serializer = AcademicResultSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = AcademicResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
