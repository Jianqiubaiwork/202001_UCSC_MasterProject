from django.urls import path

from .views import *

app_name = 'scenarios'
urlpatterns = [
    path('', scenarios_view, name='scenarios')
]