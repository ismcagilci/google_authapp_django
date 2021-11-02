from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class plantModel(models.Model):
    common = models.CharField(max_length=200,null=True)
    botanical = models.CharField(max_length=200,null=True)
    zone = models.CharField(max_length=200,null=True)
    ligth = models.CharField(max_length=200,null=True)
    price = models.CharField(max_length=200,null=True)
    availability = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.common
    
