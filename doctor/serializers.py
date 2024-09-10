from rest_framework import serializers
from doctor.models import DoctorModel,DoctorAvailableTime

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'
        
        
class DoctorAvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailableTime
        fields = '__all__'