from django.contrib import admin
from .models import * 

# Register your models here.
class Admin(admin.ModelAdmin):
    pass
admin.site.register(LoanAllocationAnswerModel, Admin)
admin.site.register(BailJudgementAnswerModel, Admin)