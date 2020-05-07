from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('bail_judgement_survey/', BailJudgementOverView.as_view(), name='bail_judgement_overview'),
    path('bail_judgement_survey/<int:id>/', BailJudgementDetailView.as_view(), name='bail_judgement_detail'),
]