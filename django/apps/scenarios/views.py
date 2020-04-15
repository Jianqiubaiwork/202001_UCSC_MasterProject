from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import *

# Create your views here.
class LoanAllocationView(TemplateView):
    template_name = 'loan_allocation.html'

    def get(self, request):
        loan_allocation_form = LoanAllocationForm()
        context = {
            'loan_allocation_form' : loan_allocation_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        loan_allocation_form = LoanAllocationForm(request.POST)
        if loan_allocation_form.is_valid():
            loan_allocation_form.save()
            return HttpResponseRedirect("/http202/")
        else:
            print(loan_allocation_form.errors)
        context = {
            'loan_allocation_form' : loan_allocation_form
        }
        return render(request, self.template_name, context)


class BailJudgementView(TemplateView):
    template_name = 'bail_judgement.html'

    def get(self, request):
        bail_judgment_form = BailJudgementForm()
        context = {
            'bail_judgment_form' : bail_judgment_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        bail_judgement_form = BailJudgementForm(request.POST)
        if bail_judgement_form.is_valid():
            bail_judgement_form.save()
            return HttpResponseRedirect("/http202/")
        else:
            print(bail_judgement_form.errors)
        context = {
            'bail_judgement_form' : bail_judgement_form
        }
        return render(request, self.template_name, context)