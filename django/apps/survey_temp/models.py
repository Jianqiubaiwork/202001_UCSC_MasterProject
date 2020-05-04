from django.db import models

# Create your models here.
class LoanAllocationAnswerModel(models.Model):
    one_one_score = models.IntegerField(default=-1)
    one_two_score = models.IntegerField(default=-1)
    one_three_score = models.IntegerField(default=-1)
    two_one_score = models.IntegerField(default=-1)
    two_two_score = models.IntegerField(default=-1)
    two_three_score = models.IntegerField(default=-1)


class BailJudgementAnswerModel(models.Model):
    one_one_score = models.IntegerField(default=-1)
    two_one_score = models.IntegerField(default=-1)
    three_one_score = models.IntegerField(default=-1)
    four_one_score = models.IntegerField(default=-1)

    one_two_score = models.IntegerField(default=-1)
    two_two_score = models.IntegerField(default=-1)
    three_two_score = models.IntegerField(default=-1)
    four_two_score = models.IntegerField(default=-1)