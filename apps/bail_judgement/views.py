from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.core.paginator import Paginator

from .forms import *
from .models import *

import random
import json
import datetime


class ModelView(TemplateView):
    template_name = 'model.html'

    def get(self, request):
        trained_models = TrainedModel.objects.all()
        count = trained_models.count()
        context = {
            'trained_models' : trained_models,
            'count' : count
        }
        return render(request, self.template_name, context)

    
    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)


class SurveyView(TemplateView):
    template_name = 'survey.html'

    def get(self, request):
        # random select 10 rows
        # FIXME: 10 is hard coded
        rand_objs = random.choices(CompasModel.objects.all(), k=10)

        # count trained models number
        all_trained_models_num = TrainedModel.objects.all().count()
        for rand_obj in rand_objs:
            rand_obj.days = rand_obj.c_jail_out - rand_obj.c_jail_in
            #rand_obj.days = rand_obj.days.days

            # get corresponding predictions of selected row
            rand_obj.predictions = CompasPredictionModel.objects.get(id=rand_obj.id)

            # random selected two prediction of all predictions
            # FIXME: 2 is hard coded
            rand_trained_models_indicies = random.sample([1, 2, 3], 2)
            rand_trained_models_indicies.sort()

            # FIXME: need extacly three models
            rand_obj.predictions.one = None
            rand_obj.predictions.two = None
            rand_obj.predictions.three = None
            if 1 not in rand_trained_models_indicies:
                rand_obj.predictions.A = rand_obj.predictions.predictor2_prob
                rand_obj.predictions.A_id = 2
                rand_obj.predictions.B = rand_obj.predictions.predictor3_prob
                rand_obj.predictions.B_id = 3
            elif 2 not in rand_trained_models_indicies:
                rand_obj.predictions.A = rand_obj.predictions.predictor1_prob
                rand_obj.predictions.A_id = 1
                rand_obj.predictions.B = rand_obj.predictions.predictor3_prob
                rand_obj.predictions.B_id = 3
            elif 3 not in rand_trained_models_indicies:
                rand_obj.predictions.A = rand_obj.predictions.predictor1_prob
                rand_obj.predictions.A_id = 1
                rand_obj.predictions.B = rand_obj.predictions.predictor2_prob
                rand_obj.predictions.B_id = 2
        paginator = Paginator(rand_objs, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj' : page_obj,
            'range' : [number for number in range (1, 11)],
            'rand_trained_models_indicies' : rand_trained_models_indicies,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        if request.is_ajax():
            survey_data = request.POST.get('survey_data', None)
            survey_data = json.loads(survey_data)
            for i in range (1, 11):
                try:
                    case_id = survey_data[str(i)]['case_id']
                    model_id = survey_data[str(i)]['model_id']
                    survey_model, created = SurveyModel.objects.get_or_create(
                        case_id=case_id
                    )
                    if int(model_id) == 1:
                        survey_model.model_one += 1
                    elif int(model_id) == 2:
                        survey_model.model_two += 1
                    elif int(model_id) == 3:    
                        survey_model.model_three += 1
                    survey_model.save()
                except KeyError:
                    pass 
            
        else:
            print("Not Ajax")
        context = {

        }
        return render(request, self.template_name, context)


class DataView(TemplateView):
    template_name = 'data.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)