from django.contrib import admin
from . import models


admin.site.register(models.Profile)


@admin.register(models.Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_expenses', 'expenses_type', 'expenses',
                    'amount_income', 'income_type', 'income', 'balance',
                    'timestamp')
