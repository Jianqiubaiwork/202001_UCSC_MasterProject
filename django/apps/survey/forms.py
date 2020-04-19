from django import forms

from .models import *

class LoanAllocationAnswerForm(forms.ModelForm):
    class Meta:
        model = LoanAllocationAnswerModel
        fields = [
            'one_one_score',
            'one_two_score',
            'one_three_score',
            'two_one_score',
            'two_two_score',
            'two_three_score'
        ]
        labels = {
            'one_one_score' : 'Your answer for question 1 in study 1',
            'one_two_score' : 'Your answer for question 2 in study 1',
            'one_three_score' : 'Your answer for question 3 in study 1',
            'two_one_score' : 'Your answer for question 1 in study 2',
            'two_two_score' : 'Your answer for question 2 in study 2',
            'two_three_score' : 'Your answer for question 3 in study 2'
        }
        widgets = {
            'one_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'one_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'one_three_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'two_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'two_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'two_three_score' : forms.NumberInput(attrs={'style': 'width: 80%'})
        }


class BailJudgementAnswerForm(forms.ModelForm):
    class Meta:
        model = BailJudgementAnswerModel
        fields = [
            'one_one_score',
            'one_two_score',
            'two_one_score',
            'two_two_score',
            'three_one_score',
            'three_two_score',
            'four_one_score',
            'four_two_score'
        ]
        labels = {
            'one_one_score' : "Borden's risk score",
            'one_two_score' : "Prater's risk score",
            'two_one_score' : "Parker's risk score",
            'two_two_score' : "Fugett's risk score",
            'three_one_score' : "Williams's risk score",
            'three_two_score' : "Lugo's risk score",
            'four_one_score' : "Cannon's risk score",
            'four_two_score' : "Rivelli's risk score"
        }
        widgets = {
            'one_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'one_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'two_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'two_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'three_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'three_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'four_one_score' : forms.NumberInput(attrs={'style': 'width: 80%'}),
            'four_two_score' : forms.NumberInput(attrs={'style': 'width: 80%'})
        }