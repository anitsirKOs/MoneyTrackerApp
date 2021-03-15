from django.test import TestCase
from tracker.forms import AddIncomeForm, AddExpensesForm


class AddIncomeFormTest(TestCase):

    def test_add_min_income_field(self):
        form = AddIncomeForm()
        self.assertFalse(form.fields['amount_income'] == 0)


class AddExpensesFormTest(TestCase):

    def test_add_min_expenses_field(self):
        form = AddExpensesForm()
        self.assertFalse(form.fields['amount_expenses'] == -2)

