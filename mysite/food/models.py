from django.db import models
from rest_framework import serializers
# Create your models here.

class UserData(models.Model):
    location = models.CharField(max_length = 100)
    search_radius = models.IntegerField()
    star_standard = models.DecimalField(decimal_places=1,max_digits=2)
