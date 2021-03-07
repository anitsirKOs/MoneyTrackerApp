from django.forms import ModelForm
from .models import Tracker


class AddIncomeForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ('amount', 'income_type')


class AddExpensesForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ('amount', 'expenses_type')
