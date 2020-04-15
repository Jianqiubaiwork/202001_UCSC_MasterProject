from django.views.generic import TemplateView
from django.shortcuts import render

from apps.scenarios.models import *

# Create your views here.
class DataView(TemplateView):
    template_name = 'data.html'

    def get(self, request):
        all_loan_allocation_models = LoanAllocationModel.objects.all()
        all_bail_judgement_models = BailJudgementModel.objects.all()
        context = {
            'all_loan_allocation_models' : all_loan_allocation_models,
            'all_bail_judgement_models' : all_bail_judgement_models
        }
        return render(request, self.template_name, context)
