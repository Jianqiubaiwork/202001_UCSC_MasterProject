from django.urls import path

from .views import *

app_name = 'design'
urlpatterns = [
    path('loan_allocation_design/', LoanAllocationDesignView.as_view(), name='loan_allocation_design'),
    path('bail_judgement_design/', BailJudgementDesignView.as_view(), name='bail_judgement_design'),
]