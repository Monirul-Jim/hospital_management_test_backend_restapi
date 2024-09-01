from django.shortcuts import render
from rest_framework import viewsets
from contact_us.models import ContactModel
from contact_us.serializers import ContactUsSerializers
# Create your views here.
class ContactUsViewSet(viewsets.ModelViewSet):
    
    queryset=ContactModel.objects.all()
    serializer_class=ContactUsSerializers