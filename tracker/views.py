import decimal
from django.shortcuts import render, redirect
from . import models
from . import forms


def home(request):
    all_tracking_data = models.Tracker.objects.filter(user=request.user).first()
    return render(request, 'tracker/home.html',
                  {'title': 'Money tracker',
                   'all_tracking_data': all_tracking_data})


def add_info(request):
    return render(request, 'tracker/add_info.html')


def add_expenses(request):
    tracker = models.Tracker.objects.all()
    if request.method == "POST":
        form = forms.AddExpensesForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('amount')
            expenses_type = request.POST.get('expenses_type')
            new_expense = models.Tracker(amount=amount,
                                         expenses_type=expenses_type,
                                         user=request.user)
            new_expense.save()
            for data in tracker:
                data.balance -= decimal.Decimal(amount)
                data.expenses += decimal.Decimal(amount)
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
            amount = request.POST.get('amount')
            income_type = request.POST.get('income_type')
            new_income = models.Tracker(amount=amount,
                                        income_type=income_type,
                                        user=request.user)
            new_income.save()
            for data in tracker:
                data.balance += decimal.Decimal(amount)
                data.income += decimal.Decimal(amount)
                data.save()

            return redirect('add_info')
    else:
        form = forms.AddIncomeForm()
        return render(request,
                      'tracker/add_income.html',
                      {'income_form': form})


def login(request):
    pass
