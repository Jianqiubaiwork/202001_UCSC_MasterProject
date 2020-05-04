from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import *

# Create your views here.
class LoanAllocationSurveyView(TemplateView):
    template_name = 'loan_allocation_survey.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class BailJudgementSurveyView(TemplateView):
    template_name = 'bail_judgement_survey.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)
        bail_judgement_answer_form = BailJudgementAnswerForm(request.POST)
        if bail_judgement_answer_form.is_valid():
            bail_judgement_answer_form.save()
            return HttpResponseRedirect("/http202/")
        else:
            print(bail_judgement_answer_form.errors)
        context = {
            'bail_judgement_answer_form' : bail_judgement_answer_form
        }
        return render(request, self.template_name, context)