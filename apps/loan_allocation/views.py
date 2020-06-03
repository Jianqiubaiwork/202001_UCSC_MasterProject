from django.shortcuts import render
from django.views.generic import TemplateView


from .forms import *
from .models import *

# Create your views here.


class ModelView(TemplateView):
    template_name = 'model.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
        context = {

        }
        return render(request, self.template_name, context)

    
class SurveyView(TemplateView):
    template_name = 'survey.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


    def post(self, request):
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