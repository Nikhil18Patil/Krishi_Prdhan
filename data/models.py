from django.db import models
from django.contrib.auth.models import User



class contactus(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=254)
    Subject=models.CharField(max_length=255)
    Message=models.CharField(max_length=500,null=True, blank=True)

class emails(models.Model):
    Email=models.EmailField(max_length=244)  
# Create your models here.

class news(models.Model):
    newstitle=models.CharField(max_length=255)
    newsdescription=models.TextField()
    

class Cropdetail(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    area = models.FloatField()
    season = models.CharField(max_length=100)     