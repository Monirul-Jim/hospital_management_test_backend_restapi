from django.contrib import admin
from appointment.models import AppointmentModel

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor_name','patient_name','appointment_types','appointment_status','symptoms','time','cancel']
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self,obj):
        return obj.doctor.name.first_name
admin.site.register(AppointmentModel,AppointmentAdmin)