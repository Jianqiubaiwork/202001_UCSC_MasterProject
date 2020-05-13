from django import forms
from .models import *



class BailJudgementFullForm(forms.ModelForm):
    class Meta:
        model = BailJudgementModel
        fields = (
            'name',
            'sex',
            'age',
            'race',
            'priors_count',
            'r_charge_desc',
            'decile_score',
            'label',
            'is_fair', 
            )


class BailJudgementVoteForm(forms.ModelForm):
    class Meta:
        model = BailJudgementModel
        fields = (
            'is_fair', 
            )