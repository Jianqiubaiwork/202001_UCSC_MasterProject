from django.urls import path

from .views import *

app_name = 'data'
urlpatterns = [
    path('', DataView.as_view(), name='data'),
]