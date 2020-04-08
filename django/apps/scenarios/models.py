from django.db import models

# Create your models here.
class LoanAllocationModel(models.Model):
    one_one_score = models.IntegerField(default=-1)
    one_two_score = models.IntegerField(default=-1)
    one_three_score = models.IntegerField(default=-1)
    two_one_score = models.IntegerField(default=-1)
    two_two_score = models.IntegerField(default=-1)
    two_three_score = models.IntegerField(default=-1)