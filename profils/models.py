from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255 , null=True ,blank=True)
    title = models.CharField(max_length=255 , null=True ,blank=True)
    fac = models.CharField(max_length=255 , null=True ,blank=True)
    facebook = models.CharField(max_length=255 , null=True)
    linkedin = models.CharField(max_length=255 , null=True)
    CIN = models.IntegerField(null=True ,blank=True , unique=True)
    email = models.CharField(max_length=255 , null=True ,blank=True)
    description = models.TextField(null=True ,blank=True)
    phone = models.IntegerField(null=True ,blank=True , unique=True)
    face = models.ImageField(upload_to='faces/', null=True ,blank=True)
    verfied = models.BooleanField(default=True , blank=True , null=True)
    
    def __str__(self):
        return f"{self.name}--->{self.CIN}"




