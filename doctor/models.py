from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DoctorSpecialization(models.Model):
    
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    def __str__(self):
        return self.name
    
    
class DoctorDesignation(models.Model):
    
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    
    def __str__(self):
        return self.name
    
class DoctorAvailableTime(models.Model):
    
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class DoctorModel(models.Model):
    
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='doctor/image')
    designation=models.ManyToManyField(DoctorDesignation)
    specialization=models.ManyToManyField(DoctorSpecialization)
    available_time=models.ManyToManyField(DoctorAvailableTime)
    fee=models.IntegerField()
    meet_link=models.CharField(max_length=100)
    
    
    def __str__(self):
        return f' {self.name.first_name} {self.name.last_name}'