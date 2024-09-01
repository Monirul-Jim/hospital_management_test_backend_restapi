from rest_framework import serializers
from service.models import ServiceModels

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModels
        fields = '__all__'