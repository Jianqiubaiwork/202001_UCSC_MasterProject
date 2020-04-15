from django.urls import path

from .views import *

app_name = 'scenarios'
urlpatterns = [
    path('loan_allocation/', LoanAllocationView.as_view(), name='loan_allocation'),
    path('bail_judgement/', BailJudgementView.as_view(), name='bail_judgement'),
]