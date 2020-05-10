from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('', OverView.as_view(), name='overview'),
    path('survey/bail_judgement/', BailJudgementOverView.as_view(), name='bail_judgement_overview'),
    path('survey/bail_judgement/<int:id>/', BailJudgementDetailView.as_view(), name='bail_judgement_detail'),
]