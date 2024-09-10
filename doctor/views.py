from django.shortcuts import render
from doctor.serializers import DoctorSerializers,DoctorAvailableTimeSerializers
from doctor.models import DoctorModel,DoctorAvailableTime
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,BasePermission,IsAuthenticatedOrReadOnly
# from common.permissions import IsAuthenticatedCustom
# Create your views here.

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_query_set(self,request,query_set,view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class DoctorAvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailableTime.objects.all()
    serializer_class = DoctorAvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers
    permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedCustom]