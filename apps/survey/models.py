from django.db import models
from postgres_copy import CopyManager

# Create your models here.
class LoanAllocationCSVModel(models.Model):
    name = models.CharField(max_length=50)
    race = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    repayment_rate = models.IntegerField(null=True)
    objects = CopyManager()


class BailJudgementCSVModel(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    prior_offsenses = models.CharField(max_length=500)
    subsequent_offenses = models.CharField(max_length=500)
    risk_score = models.IntegerField(null=True)
    objects = CopyManager()