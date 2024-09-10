from django.shortcuts import render
from doctor.serializers import DoctorSerializers
from doctor.models import DoctorModel
from rest_framework import viewsets
from common.permissions import IsAuthenticatedCustom
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers
    permission_classes=[IsAuthenticatedCustom]