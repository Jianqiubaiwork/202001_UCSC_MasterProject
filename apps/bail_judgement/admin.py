from django.contrib import admin
from .models import * 
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#class Admin(admin.ModelAdmin):
#    pass
#admin.site.register(BailJudgementModel, AuthorAdmin)

@admin.register(CompasModel)
#@admin.register(CompasPredictionModel)
@admin.register(TrainedModel)
@admin.register(SurveyQueueModel)
class ViewAdmin(ImportExportModelAdmin):
    pass