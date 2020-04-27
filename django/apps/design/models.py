from django.db import models

# Create your models here.
class LoanAllocationDesignModel(models.Model):

    GENDER_LIST = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    RACE_LIST = [
        ('American Indian or Alaska Native', 'American Indian or Alaska Native'),
        ('Asian', 'Asian'),
        ('Black or African American', 'Black or African American'),
        ('Hispanic or Latino', 'Hispanic or Latino'),
        ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'),
        ('White', 'White')
    ]


    name = models.CharField(null=True, blank=True, max_length=100)
    gender = models.CharField(
        #choices=GENDER_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    race = models.CharField(
        #choices=RACE_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    age = models.IntegerField()
    rate = models.IntegerField()