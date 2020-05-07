from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.conf import settings

from .forms import *
from .models import *


class BailJudgementOverView(TemplateView):
    template_name = 'bail_judgement_overview.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class BailJudgementDetailView(TemplateView):
    template_name = 'bail_judgement_detail.html'

    def get(self, request, id):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        context = {
        }
        return render(request, self.template_name, context)


'''
DATA = [
        {
            'id' : 1,
            'name' : 'Alias',
            'race' : 'Asian',
            'age' : 24,
            'repayment_rate' : 60,
            'located_money_1' : 50,
            'located_money_2' : 20,
        },
        {
            'id' : 2,
            'name' : 'Bob',
            'race' : 'American',
            'age' : 36,
            'repayment_rate' : 80,
            'located_money_1' : 50,
            'located_money_2' : 80
        },
        {
            'id' : 3,
            'name' : 'Cay',
            'race' : 'Italian',
            'age' : 16,
            'repayment_rate' : 100,
            'located_money_1' : 50,
            'located_money_2' : 10
        },
        {
            'id' : 4,
            'name' : 'Dodge',
            'race' : 'English',
            'age' : 21,
            'repayment_rate' : 20,
            'located_money_1' : 50,
            'located_money_2' : 10
        },
        {
            'id' : 5,
            'name' : 'Foo',
            'race' : 'French',
            'age' : 24,
            'repayment_rate' : 60,
            'located_money_1' : 50,
            'located_money_2' : 75
        },
        {
            'id' : 6,
            'name' : 'Ray',
            'race' : 'Asian',
            'age' : 50,
            'repayment_rate' : 100,
            'located_money_1' : 50,
            'located_money_2' : 25
        }
    ]


def get_obj_A_by_id(data, id):
    obj = None
    obj = next((obj for obj in data if obj['id'] == id - 1), None)
    return obj

def get_obj_B_by_id(data, id):
    obj = None
    obj = next((obj for obj in data if obj['id'] == id), None)
    return obj


# Create your views here.
class LoanAllocationOverView(TemplateView):
    template_name = 'loan_allocation_overview_static.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)

class LoanAllocationDetailView(TemplateView):
    template_name = 'loan_allocation_detail_static.html'

    def get(self, request, pair_id):
        context = {
            'title' : 'loan_allocation_static.csv',
            'obj_A' : get_obj_A_by_id(DATA, pair_id * 2),
            'obj_B' : get_obj_B_by_id(DATA, pair_id * 2)
        }
        return render(request, self.template_name, context)

    def post(self, request, pair_id):
        context = {
        }
        return render(request, self.template_name, context)


'''