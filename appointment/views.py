from django.shortcuts import render
from appointment.serializers import AppointmentSerializers
from appointment.models import AppointmentModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializers
    # custom query
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "success": True,
                "message": "Appointments fetched successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "success": False,
                "message": "Appointments Api Not Found !!",
                "error": ""
            }, status=status.HTTP_404_NOT_FOUND)