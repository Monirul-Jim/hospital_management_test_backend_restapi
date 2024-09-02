from rest_framework import serializers
from patient.models import PatientModel

class PatientSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model = PatientModel
        fields = '__all__'