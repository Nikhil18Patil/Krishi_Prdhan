from django.db import models
from django.contrib.auth.models import User

class mynews(models.Model):
    newstitle=models.CharField(max_length=255)
    newsdescription=models.TextField()    
    class Meta:
        db_table='itsnews'
# Create your models here.
