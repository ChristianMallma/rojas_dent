from django.contrib import admin
from .models import ClinicalCases, ClinicalCasesDetail


# Register your models here.
class ClinicalCasesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at', 'updated_at', 'title')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'


class ClinicalCasesDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('created_at', 'updated_at')
    ordering = ('-created_at', 'updated_at')


admin.site.register(ClinicalCasesDetail, ClinicalCasesDetailAdmin)
