from django.shortcuts import render
from doctor.serializers import DoctorSerializers
from doctor.models import DoctorModel
from rest_framework import viewsets
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers