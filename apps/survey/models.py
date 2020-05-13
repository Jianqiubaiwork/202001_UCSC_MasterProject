from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class BailJudgementModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    sex = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    race_choices = {
        ('African-American', 'African-American'),
        ('Caucasian', 'Caucasian'),
        ('Hispanic', 'Hispanic'),
        ('Other', 'Ohter')
    }

    race = models.CharField(max_length=50, choices=race_choices, default='African-American')
    priors_count = models.IntegerField(blank=True, null=True)
    r_charge_desc = models.CharField(max_length=255)
    decile_score = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)
    is_fair = models.BooleanField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} | {self.sex} | {self.age} | {self.race}"
