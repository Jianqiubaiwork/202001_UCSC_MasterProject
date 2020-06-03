from django.urls import path

from .views import *

app_name = 'loan_allocation'
urlpatterns = [
    path('', ModelView.as_view(), name='model'),
    path('survey/', SurveyView.as_view(), name='survey'),
    path('data/', DataView.as_view(), name='data'),
    path('model/', ModelView.as_view(), name='model'),
]