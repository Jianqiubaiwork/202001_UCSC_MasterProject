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
        self.fields['name_A'] = forms.CharField(required=False)
        self.fields['gender_A'] = forms.ChoiceField(
            choices=get_gender_choices() )
        #self.fields['gender_A'].widget.attrs['style'] = 'width:40%;'
        self.fields['race_A'] = forms.ChoiceField(
            choices=get_race_choices() )
        self.fields['race_A'].widget.attrs['style'] = 'width:40%;'

        self.fields['name_B'] = forms.CharField(required=False)
        self.fields['gender_B'] = forms.ChoiceField(
            choices=get_gender_choices() )
        #self.fields['gender_B'].widget.attrs['style'] = 'width:40%;'
        self.fields['race_B'] = forms.ChoiceField(
            choices=get_race_choices() )
        self.fields['race_B'].widget.attrs['style'] = 'width:40%;'

    class Meta:
        model = LoanAllocationDesignModel
        fields = [
            'money_in_total',
            'name_A',
            'gender_A',
            'race_A',
            'rate_A',
            'age_A',
            'money_A',
            'name_B',
            'gender_B',
            'race_B',
            'rate_B',
            'age_B',
            'money_B'
        ]
        labels = {
            'name_A' : 'Name',
            'gender_A' : 'Gender',
            'race_A' : 'Race',
            'rate_A' : 'Rate (%)',
            'age_A' : 'Age',
            'name_B' : 'Name',
            'gender_B' : 'Gender',
            'race_B' : 'Race',
            'rate_B' : 'Rate (%)',
            'age_B' : 'Age'
        }
        widgets = {
            'money_in_total' : forms.NumberInput(attrs={'placeholder' : '1,000.00'}),
            'name_A' : forms.TextInput(attrs={'style': 'width: 40%', 'placeholder' : 'custom name'}),
            #'gender_A' : forms.Select(attrs={'style': 'width: 40%'}),
            #'race_A' : forms.Select(attrs={'style': 'width: 40%'}),
            #'rate_A' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '0','max': '100'}),
            #'age_A' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '16','max': '99'}),
            'name_B' : forms.TextInput(attrs={'style': 'width: 40%', 'placeholder' : 'custom name'}),
            #'gender_B' : forms.Select(attrs={'style': 'width: 40%'}),
            #'race_B' : forms.Select(attrs={'style': 'width: 40%'}),
            #'rate_B' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '0','max': '100'}),
            #'age_B' : forms.NumberInput(attrs={'style': 'width: 80%', 'min': '16','max': '99'})
        }
        

    def clean_age_A(self):
        age_A = self.cleaned_data.get('age_A')
        if age_A < 16 or age_A > 99:
            raise forms.ValidationError("Invalid age_A!")
        else:
            return age_A

    
    def clean_age_B(self):
        age_B = self.cleaned_data.get('age_B')
        if age_B < 16 or age_B > 99:
            raise forms.ValidationError("Invalid age_B!")
        else:
            return age_B


    def clean_rate_A(self):
        rate_A = self.cleaned_data.get('rate_A')
        if rate_A < 0 or rate_A > 100:
            raise forms.ValidationError("Invalid rate_A!")
        else:
            return rate_A


    def clean_rate_B(self):
        rate_B = self.cleaned_data.get('rate_B')
        if rate_B < 0 or rate_B > 100:
            raise forms.ValidationError("Invalid rate_B!")
        else:
            return rate_B