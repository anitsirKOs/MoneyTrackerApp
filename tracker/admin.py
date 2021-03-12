from django.contrib import admin
from . import models


@admin.register(models.Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_expenses', 'expenses_type', 'expenses',
                    'amount_income', 'income_type', 'income', 'balance',
                    'date', 'timestamp')
