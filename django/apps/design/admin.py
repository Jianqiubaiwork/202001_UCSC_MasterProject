from django.contrib import admin
from .models import * 

# Register your models here.
class Admin(admin.ModelAdmin):
    pass
admin.site.register(LoanAllocationDesignModel, Admin)
admin.site.register(BailJudgementDesignModel, Admin)
