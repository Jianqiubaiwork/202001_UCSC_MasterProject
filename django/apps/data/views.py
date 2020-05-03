from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect

from apps.design.models import *
from apps.survey.models import *

# Create your views here.
class DataView(TemplateView):
    template_name = 'data.html'

    def get(self, request):
        all_loan_allocation_design_models = LoanAllocationDesignModel.objects.all()
        #all_bail_judgement_answer_models = BailJudgementAnswerModel.objects.all()
        context = {
            'all_loan_allocation_design_models' : all_loan_allocation_design_models,
        #    'all_bail_judgement_answer_models' : all_bail_judgement_answer_models
        }
        return render(request, self.template_name, context)
        #return HttpResponseRedirect('/comming_soon')
