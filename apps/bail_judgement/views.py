from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.core.paginator import Paginator

from .forms import *
from .models import *


import random


class ModelView(TemplateView):
    template_name = 'model.html'

    def get(self, request):
        trained_models = TrainedModel.objects.all()
        context = {
            'trained_models' : trained_models,
        }
        return render(request, self.template_name, context)

    
    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)


class SurveyView(TemplateView):
    template_name = 'survey.html'

    def get(self, request):
        #count = CompasModel.objects.count()
        #rand_obj = CompasModel.objects.all()[randint(0, count - 1)] #single random object
        rand_objs = random.choices(CompasModel.objects.all(), k=10)
        paginator = Paginator(rand_objs, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj' : page_obj,
        }
        return render(request, self.template_name, context)


'''
class BailJudgementOverView(TemplateView):
    template_name = 'bail_judgement_overview.html'

    def get(self, request):
        objs = BailJudgementModel.objects.all()
        context = {
            'objs' : objs,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class BailJudgementDetailView(TemplateView):
    template_name = 'bail_judgement_detail.html'

    def get(self, request, id):
        obj = get_object_or_404(BailJudgementModel, id=id)
        #bail_judgement_full_form = BailJudgementFullForm()
        context = {
            'obj' : obj,
            #'bail_judgement_full_form' : bail_judgement_full_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        obj = get_object_or_404(BailJudgementModel, id=id)
        bail_judgement_full_form = BailJudgementFullForm(request.POST)
        if bail_judgement_full_form.is_valid():
            bail_judgement_full_form.save()
            print('success')
            return redirect('/survey/bail_judgement')
        else:
            print(bail_judgement_full_form.errors)
        context = {
            'obj' : obj,
            #'bail_judgement_full_form' : bail_judgement_full_form,
        }
        return render(request, self.template_name, context)


class LoanAllocationOverView(TemplateView):
    template_name = 'loan_allocation_overview.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
        }
        return render(request, self.template_name, context)


class LoanAllocationDetailView(TemplateView):
    template_name = 'loan_allocation_detail.html'

    def get(self, request, id):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        context = {
        }
        return render(request, self.template_name, context)


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





'''