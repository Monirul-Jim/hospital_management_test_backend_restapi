from rest_framework import serializers
from appointment.models import AppointmentModel
from patient.models import PatientModel
from doctor.models import DoctorAvailableTime, DoctorModel

class AppointmentSerializers(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientModel.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=DoctorModel.objects.all())
    time = serializers.PrimaryKeyRelatedField(queryset=DoctorAvailableTime.objects.all())
    # patient=serializers.StringRelatedField(many=False)
    # doctor=serializers.StringRelatedField(many=False)
    # time=serializers.StringRelatedField(many=False)
    class Meta:
        model = AppointmentModel
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['patient'] = instance.patient.user.first_name + ' ' + instance.patient.user.last_name
        representation['doctor'] =  instance.doctor.name.first_name + ' ' + instance.doctor.name.last_name
        representation['time'] = str(instance.time)
        return representation