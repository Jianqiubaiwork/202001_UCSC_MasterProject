from django.urls import path

from .views import *

app_name = 'bail_judgement'
urlpatterns = [
    path('', ModelView.as_view(), name='model'),
    path('survey/', SurveyView.as_view(), name='survey'),
    #path('bail_judgement/<int:id>/', BailJudgementDetailView.as_view(), name='bail_judgement_detail'),
    #path('loan_allocation/', LoanAllocationOverView.as_view(), name='loan_allocation_overview'),
    #path('loan_allocation/<int:id>/', LoanAllocationDetailView.as_view(), name='loan_allocation_detail'),
]