from django.db import models

# Create your models here.
class ServiceModels(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='service/images/')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Service'