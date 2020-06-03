from django.urls import path

from .views import *

app_name = 'bail_judgement'
urlpatterns = [
    path('', ModelView.as_view(), name='model'),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('data/', DataView.as_view(), name='data'),
    path('model/', ModelView.as_view(), name='model'),
]