from django.contrib import admin
from .models import * 

# Register your models here.
class Admin(admin.ModelAdmin):
    pass
admin.site.register(LoanAllocationCSVModel, Admin)
admin.site.register(BailJudgementCSVModel, Admin)