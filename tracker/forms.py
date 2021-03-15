from django.contrib.auth.models import User
from django import forms
from . import models


class AddIncomeForm(forms.ModelForm):
    amount_income = forms.DecimalField(min_value=0.01,
                                       error_messages={
                                           'min_value': u'Price cannot be less than 0.01'
                                       })

    class Meta:
        model = models.Tracker
        fields = ('income_type',)


class AddExpensesForm(forms.ModelForm):
    amount_expenses = forms.DecimalField(min_value=0.01,
                                         error_messages={
                                             'min_value': u'Price cannot be less than 0.01'
                                         })

    class Meta:
        model = models.Tracker
        fields = ('expenses_type',)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password']
