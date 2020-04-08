from django import forms

from .models import *

class LoanAllocationForm(forms.ModelForm):
    class Meta:
        model = LoanAllocationModel
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