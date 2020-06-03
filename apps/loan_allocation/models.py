from django.db import models

# Create your models here.

class HumanModel(models.Model):
    first_name = models.CharField(null=True, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    gender = models.CharField(null=True, max_length=10)
    job = models.CharField(null=True, max_length=100)
    job_location = models.CharField(null=True, max_length=100)
    age = models.IntegerField(null=True)
    length_service = models.IntegerField(null=True)

