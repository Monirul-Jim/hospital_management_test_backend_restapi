from django.shortcuts import render
from  rest_framework import viewsets
from service.models import ServiceModels
from service.serializers import ServiceSerializer

# Create your views here.
class ServicesViewSet(viewsets.ModelViewSet):
    queryset=ServiceModels.objects.all()
    serializer_class= ServiceSerializer
