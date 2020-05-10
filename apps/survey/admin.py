from django.contrib import admin
from .models import * 
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#class Admin(admin.ModelAdmin):
#    pass
#admin.site.register(BailJudgementModel, AuthorAdmin)

@admin.register(BailJudgementModel)
class ViewAdmin(ImportExportModelAdmin):
    pass