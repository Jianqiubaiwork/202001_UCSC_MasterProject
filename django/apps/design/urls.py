from django.urls import path

from .views import *

app_name = 'design'
urlpatterns = [
    path('', design_view, name='design')
]