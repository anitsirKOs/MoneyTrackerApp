from django.forms import DecimalField
from django.forms import ModelForm
from django.forms import SelectDateWidget

from .models import Tracker


class AddIncomeForm(ModelForm):
    amount_income = DecimalField(min_value=0.01,
                                 error_messages={
                                     'min_value': u'Price cannot be less than 0.01'
                                 })

    class Meta:
        model = Tracker
        fields = ('income_type', 'date')
        widgets = {
            'date': SelectDateWidget(),
        }


class AddExpensesForm(ModelForm):
    amount_expenses = DecimalField(min_value=0.01,
                                   error_messages={
                                       'min_value': u'Price cannot be less than 0.01'
                                   })

    class Meta:
        model = Tracker
        fields = ('expenses_type', 'date')
        widgets = {
            'date': SelectDateWidget(),
        }
