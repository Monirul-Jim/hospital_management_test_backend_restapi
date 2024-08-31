from django.contrib import admin
from . import models
# Register your models here.


class DoctorSpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ['name',]}
    
class DoctorDesignationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ['name',]}
    
    
admin.site.register(models.DoctorSpecialization,DoctorSpecializationAdmin)
admin.site.register(models.DoctorDesignation,DoctorDesignationAdmin)
admin.site.register(models.DoctorAvailableTime)
admin.site.register(models.DoctorModel)