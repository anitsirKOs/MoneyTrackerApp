from django.forms import ModelForm, SelectDateWidget
from .models import Tracker


class AddIncomeForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ('amount', 'income_type', 'date')
        widgets = {
            'date': SelectDateWidget(),
        }


class AddExpensesForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ('amount_expenses', 'expenses_type', 'date')
        widgets = {
            'date': SelectDateWidget(),
        }
