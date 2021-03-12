import decimal
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from . import models
from . import forms


def home(request):
    data = models.Tracker.objects.all()
    all_tracking_data = models.Tracker.objects.filter(user=request.user).first()

    storage = messages.get_messages(request)
    if all_tracking_data:
        if all_tracking_data.balance <= 0:
            messages.warning(request, 'You are out of budget!')

    return render(request, 'tracker/home.html',
                  {'title': 'Money tracker',
                   'data': data,
                   'all_tracking_data': all_tracking_data,
                   'warning_message': storage})


def add_info(request):
    storage = messages.get_messages(request)
    return render(request, 'tracker/add_info.html', {'messages': storage})


def add_expenses(request):
    tracker = models.Tracker.objects.all()
    if request.method == "POST":
        form = forms.AddExpensesForm(request.POST)
        if form.is_valid():
            amount_expenses = request.POST.get('amount_expenses')
            expenses_type = request.POST.get('expenses_type')
            date = request.POST.get('date')
            new_expense = models.Tracker(amount_expenses=amount_expenses,
                                         expenses_type=expenses_type,
                                         date=date,
                                         user=request.user)
            new_expense.save()
            messages.success(request, 'Your expense was added!')
            for data in tracker:
                data.balance -= decimal.Decimal(amount_expenses)
                data.expenses += decimal.Decimal(amount_expenses)
                data.save()

        return redirect('add_info')
    else:
        form = forms.AddExpensesForm()
        return render(request,
                      'tracker/add_expenses.html',
                      {'expense_form': form})


def add_income(request):
    tracker = models.Tracker.objects.all()
    if request.method == "POST":
        form = forms.AddIncomeForm(request.POST)
        if form.is_valid():
            amount_income = request.POST.get('amount_income')
            income_type = request.POST.get('income_type')
            date = request.POST.get('date')
            new_income = models.Tracker(amount_income=amount_income,
                                        income_type=income_type,
                                        date=date,
                                        user=request.user)
            new_income.save()
            messages.success(request, 'Your income was added!')
            for data in tracker:
                data.balance += decimal.Decimal(amount_income)
                data.income += decimal.Decimal(amount_income)
                data.save()

        return redirect('add_info')
    else:
        form = forms.AddIncomeForm()
        return render(request,
                      'tracker/add_income.html',
                      {'income_form': form})


class ExpensesChartView(TemplateView):
    template_name = 'charts/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = models.Tracker.objects.all()
        return context
