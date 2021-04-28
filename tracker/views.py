import decimal
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import constants
from . import models
from . import forms


def show_start_page(request):
    app_key = '29f2bc1a88436bd61aab5ddde08873ee'
    url = 'https://api.openweathermap.org/data/2.5/find?q=' \
          '{}&units=metric&appid=' + app_key
    city = 'Minsk'
    response = requests.get(url.format(city)).json()
    print(response)
    city_info = {
        'city': city,
        'temp': response['list'][0]['main']['temp'],
        'humidity': response['list'][0]['main']['humidity'],
        'rain': response['list'][0]['rain'],
        'icon': response['list'][0]['weather'][0]['icon'],
    }

    context = {
        'info': city_info,
    }
    return render(request, 'registration/index.html', context)


@login_required
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


@login_required
def add_info(request):
    storage = messages.get_messages(request)
    return render(request, 'tracker/add_info.html', {'messages': storage})


@login_required
def add_expenses(request):
    tracker = models.Tracker.objects.all()
    if request.method == "POST":
        form = forms.AddExpensesForm(request.POST)
        if form.is_valid():
            amount_expenses = request.POST.get('amount_expenses')
            expenses_type = request.POST.get('expenses_type')
            new_expense = models.Tracker(amount_expenses=amount_expenses,
                                         expenses_type=expenses_type,
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


@login_required
def add_income(request):
    tracker = models.Tracker.objects.all()
    if request.method == "POST":
        form = forms.AddIncomeForm(request.POST)
        if form.is_valid():
            amount_income = request.POST.get('amount_income')
            income_type = request.POST.get('income_type')
            new_income = models.Tracker(amount_income=amount_income,
                                        income_type=income_type,
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


@login_required
def view_profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user)

            subject = constants.REGISTER_EMAIL_SUBJECT.format(
                user_form.cleaned_data['username']
            )
            body = constants.REGISTER_EMAIL_BODY
            to_email = request.POST.get('email')
            send_mail(subject, body, 'me@me.by', [to_email, ])

            messages.success(request, 'Registration completed successfully!'
                                      ' Please check your email.')
            return render(request,
                          'registration/registration_done.html',
                          {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'registration/register.html',
                  {'user_form': user_form})
