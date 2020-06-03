from django.shortcuts import render
from django.views.generic import TemplateView


from .forms import *
from .models import *

# Create your views here.


class ModelView(TemplateView):
    template_name = 'loan_model.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)

    
class SurveyView(TemplateView):
    template_name = 'loan_survey.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)


class DataView(TemplateView):
    template_name = 'loan_data.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)