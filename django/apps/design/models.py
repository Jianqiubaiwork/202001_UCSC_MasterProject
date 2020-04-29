from django.db import models

# Create your models here.
class LoanAllocationDesignModel(models.Model):

    # ========== Static List ========== #
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

    # ========== Variabls ========== #
    # money
    money_in_total = models.IntegerField()

    # person A
    name_A = models.CharField(null=True, blank=True, max_length=100)
    gender_A = models.CharField(
        #choices=GENDER_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    race_A = models.CharField(
        #choices=RACE_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    age_A = models.IntegerField()
    rate_A = models.IntegerField()
    money_A = models.IntegerField()

    # person B
    name_B = models.CharField(null=True, blank=True, max_length=100)
    gender_B = models.CharField(
        #choices=GENDER_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    race_B = models.CharField(
        #choices=RACE_LIST,
        null=True,
        blank=True,
        max_length=100
    )
    age_B = models.IntegerField()
    rate_B = models.IntegerField()
    money_B = models.IntegerField()