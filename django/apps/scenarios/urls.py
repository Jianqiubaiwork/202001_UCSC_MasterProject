from django.urls import path

from .views import *

app_name = 'scenarios'
urlpatterns = [
    path('loan_allocation/', loan_allocation_view, name='loan_allocation'),
]