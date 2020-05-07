from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('loan_allocation_survey/', LoanAllocationOverView.as_view(), name='loan_allocation_overview'),
    path('loan_allocation_survey/<int:pair_id>/', LoanAllocationDetailView.as_view(), name='loan_allocation_detail'),
    path('bail_judgement_survey/', BailJudgementOverView.as_view(), name='bail_judgement_overview'),
    path('bail_judgement_survey/<int:id>/', BailJudgementDetailView.as_view(), name='bail_judgement_detail'),
]