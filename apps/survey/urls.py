from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('', OverView.as_view(), name='overview'),
    path('bail_judgement/', BailJudgementOverView.as_view(), name='bail_judgement_overview'),
    path('bail_judgement/<int:id>/', BailJudgementDetailView.as_view(), name='bail_judgement_detail'),
    path('loan_allocation/', LoanAllocationOverView.as_view(), name='loan_allocation_overview'),
    path('loan_allocation/<int:id>/', LoanAllocationDetailView.as_view(), name='loan_allocation_detail'),
]