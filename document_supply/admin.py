from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Apply_user
# Register your models here.

class Apply_userAdmin(ImportExportMixin, admin.ModelAdmin) :
    pass

admin.site.register(Apply_user, Apply_userAdmin)