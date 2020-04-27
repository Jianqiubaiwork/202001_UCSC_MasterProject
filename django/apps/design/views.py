from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import *

# Create your views here.
class LoanAllocationDesignView(TemplateView):
    template_name = 'loan_allocation_design.html'

    def get(self, request):
        loan_allocation_design_form_A = LoanAllocationDesignForm()
        loan_allocation_design_form_B = LoanAllocationDesignForm()
        context = {
            'loan_allocation_design_form_A' : loan_allocation_design_form_A,
            'loan_allocation_design_form_B' : loan_allocation_design_form_B
        }
        return render(request, self.template_name, context)

    def post(self, request):
        loan_allocation_design_form_A = LoanAllocationDesignForm(request.POST)
        loan_allocation_design_form_B = LoanAllocationDesignForm(request.POST)
        if loan_allocation_design_form_A.is_valid():
            loan_allocation_design_form_A.save()
            return HttpResponseRedirect("/http202/")
        else:
            print(loan_allocation_design_form_A.errors)
        if loan_allocation_design_form_B.is_valid():
            loan_allocation_design_form_B.save()
            return HttpResponseRedirect("/http202/")
        else:
            print(loan_allocation_design_form_B.errors)
        context = {
            'loan_allocation_design_form_A' : loan_allocation_design_form_A,
            'loan_allocation_design_form_B' : loan_allocation_design_form_B
        }
        return render(request, self.template_name, context)


class BailJudgementDesignView(TemplateView):
    template_name = 'bail_judgement_design.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)