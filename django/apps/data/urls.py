from django.urls import path

from .views import *

app_name = 'data'
urlpatterns = [
    path('', data_view, name='data'),
]