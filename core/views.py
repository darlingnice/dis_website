from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AcademicYear, SchoolClass, Section, Subject
from .serializers import AcademicYearSerializer, SchoolClassSerializer, SectionSerializer, SubjectSerializer

@api_view(['GET', 'POST'])
def academic_year_list_create(request):
    if request.method == 'GET':
        queryset = AcademicYear.objects.all()
        serializer = AcademicYearSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = AcademicYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def class_list_create(request):
    if request.method == 'GET':
        queryset = SchoolClass.objects.all()
        serializer = SchoolClassSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = SchoolClassSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def section_list_create(request):
    if request.method == 'GET':
        queryset = Section.objects.all()
        serializer = SectionSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = SectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def subject_list_create(request):
    if request.method == 'GET':
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data)

    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
