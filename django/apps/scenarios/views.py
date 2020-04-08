from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import *

# Create your views here.
def loan_allocation_view(request):
    context = {}
    loan_allocation_form = LoanAllocationForm(request.POST or None)
    context['loan_allocation_form'] = loan_allocation_form
    if loan_allocation_form.is_valid():
        return HttpResponseRedirect("/http202/")
    else:
        print(loan_allocation_form.errors)
    return render(request, 'loan_allocation.html', context)