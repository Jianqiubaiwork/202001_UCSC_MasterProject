from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('loan_allocation_survey/', LoanAllocationSurveyView.as_view(), name='loan_allocation_survey'),
    path('bail_judgement_survey/', BailJudgementSurveyView.as_view(), name='bail_judgement_survey'),
]