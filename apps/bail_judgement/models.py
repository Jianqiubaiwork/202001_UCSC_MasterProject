from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
RACE_CHOICES = {
    ('African-American', 'African-American'),
    ('Caucasian', 'Caucasian'),
    ('Hispanic', 'Hispanic'),
    ('Other', 'Ohter')
}

'''
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
'''

class CompasModel(models.Model):
    sex = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null=True, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    age_cat = models.CharField(null=True, max_length=100)
    race = models.CharField(null=True, max_length=50, choices=RACE_CHOICES, default='African-American')
    decile_score = models.IntegerField(null=True)
    days_b_screening_arrest = models.IntegerField(null=True)
    c_jail_in = models.DateTimeField(null=True)
    c_jail_out = models.DateTimeField(null=True)
    c_charge_degree = models.CharField(null=True, max_length=1)
    score_text = models.CharField(null=True, max_length=25)
    priors_count = models.IntegerField(null=True)
    two_year_recid = models.IntegerField(null=True)

    # prediction = models.ForeignKey(CompasPredictionModel, on_delete=CASCADE)
    predictor1 = models.IntegerField(null=True)
    predictor2 = models.IntegerField(null=True)
    predictor3 = models.IntegerField(null=True)
    predictor1_prob = models.FloatField(null=True)
    predictor2_prob = models.FloatField(null=True)
    predictor3_prob = models.FloatField(null=True)


    image_name = models.CharField(null=True, max_length=100)


    def __str__(self):
        return f"{self.id}"

'''
class CompasPredictionModel(models.Model):
    raw_id = models.IntegerField()
    predictor1 = models.IntegerField()
    predictor2 = models.IntegerField()
    predictor3 = models.IntegerField()
    predictor1_prob = models.FloatField()
    predictor2_prob = models.FloatField()
    predictor3_prob = models.FloatField()

    def __str__(self):
        return f"{self.raw_id}"
'''


class TrainedModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.description}"


class SurveyQueueModel(models.Model):
    compas_list = models.CharField(max_length=100)
    vote_list = models.CharField(max_length=100)