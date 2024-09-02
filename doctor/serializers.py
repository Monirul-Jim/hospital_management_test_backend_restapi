from rest_framework import serializers
from doctor.models import DoctorModel

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'