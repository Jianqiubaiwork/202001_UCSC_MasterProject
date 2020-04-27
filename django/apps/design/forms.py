from django import forms

from .models import *

def get_gender_choices():
    return [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

def get_race_choices():
    return [
        ('American Indian or Alaska Native', 'American Indian or Alaska Native'),
        ('Asian', 'Asian'),
        ('Black or African American', 'Black or African American'),
        ('Hispanic or Latino', 'Hispanic or Latino'),
        ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'),
        ('White', 'White')
    ]

class LoanAllocationDesignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoanAllocationDesignForm, self).__init__(*args, **kwargs)
        self.fields['gender'] = forms.ChoiceField(
            choices=get_gender_choices() )
        self.fields['gender'].widget.attrs['style'] = 'width:80%;'
        self.fields['race'] = forms.ChoiceField(
            choices=get_race_choices() )
        self.fields['race'].widget.attrs['style'] = 'width:80%;'

    class Meta:
        model = LoanAllocationDesignModel
        fields = [
            'name',
            'gender',
            'race',
            'rate',
            'age'
        ]
        labels = {
            'name' : 'Name',
            'gender' : 'Gender',
            'race' : 'Race',
            'rate' : 'Rate (%)',
            'age' : 'Age'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'style': 'width: 80%'}),
            #'gender' : forms.Select(attrs={'style': 'width: 80%'}),
            #'race' : forms.Select(attrs={'style': 'width: 80%'}),
            'rate' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '0','max': '100'}),
            'age' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '16','max': '99'})
        }
        