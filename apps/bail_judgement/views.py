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
        rand_objs = random.choices(CompasModel.objects.all(), k=10)
        #rand_model_indicies = random.choices([1, 2, 3], k=)
        all_trained_models_num = TrainedModel.objects.all().count()
        for rand_obj in rand_objs:
            rand_obj_prediction = CompasPredictionModel.objects.get(id=rand_obj.id)

            rand_trained_models_indicies = random.sample(range(1, all_trained_models_num), 2)
            rand_obj_prediction.one = None
            rand_obj_prediction.two = None
            rand_obj_prediction.three = None
            if 1 in rand_trained_models_indicies:
                rand_obj_prediction.one = rand_obj_prediction.predictor1_prob
            elif 2 in rand_trained_models_indicies:
                rand_obj_prediction.two = rand_obj_prediction.predictor2_prob
            elif 3 in rand_trained_models_indicies:
                rand_obj_prediction.three = rand_obj_prediction.predictor3_prob
        paginator = Paginator(rand_objs, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj' : page_obj,
            'page_number' : page_number,
            'rand_trained_models_indicies' : rand_trained_models_indicies,
        }
        return render(request, self.template_name, context)
