from django.views.generic import TemplateView
from django.shortcuts import render

from apps.survey.models import *

# Create your views here.
class DataView(TemplateView):
    template_name = 'temp.html'

    def get(self, request):
        #all_loan_allocation_answer_models = LoanAllocationAnswerModel.objects.all()
        #all_bail_judgement_answer_models = BailJudgementAnswerModel.objects.all()
        context = {
        #    'all_loan_allocation_answer_models' : all_loan_allocation_answer_models,
        #    'all_bail_judgement_answer_models' : all_bail_judgement_answer_models
        }
        return render(request, self.template_name, context)
