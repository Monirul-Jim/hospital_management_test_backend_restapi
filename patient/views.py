from django.shortcuts import render
from rest_framework import viewsets
from patient.models import PatientModel
from patient.serializers import PatientSerializers
# Create your views here.
class PatientViewSets(viewsets.ModelViewSet):
    queryset=PatientModel.objects.all()
    serializer_class= PatientSerializers