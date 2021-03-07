from django.contrib import admin
from . import models


@admin.register(models.Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'expenses', 'expenses_type',
                    'income', 'income_type', 'balance')
