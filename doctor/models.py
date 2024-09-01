from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel
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
    
    
STAR_CHOICES=[
    ('⭐','⭐'),
    ('⭐ ⭐ ','⭐ ⭐'),
    ('⭐ ⭐ ⭐','⭐ ⭐ ⭐'),
    ('⭐ ⭐ ⭐ ⭐','⭐ ⭐ ⭐ ⭐'),
    ('⭐ ⭐ ⭐ ⭐ ⭐','⭐ ⭐ ⭐ ⭐ ⭐'),
]
class ReviewModel(models.Model):
    reviewer=models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10,choices=STAR_CHOICES)
    
    def __str__(self):
        return f' Patient {self.reviewer.user.first_name}; Doctor : {self.doctor.name.first_name}'