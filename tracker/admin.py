from django.contrib import admin
from . import models


@admin.register(models.Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_expenses', 'expenses_type', 'amount_income',
                    'income', 'income_type', 'balance', 'date', 'timestamp')
