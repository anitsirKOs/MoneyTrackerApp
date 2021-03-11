from django.db import models
from django.contrib.auth.models import User
from . import constants


class Tracker(models.Model):
    balance = models.DecimalField(default=0, blank=True, null=True,
                                  max_digits=10, decimal_places=2)
    expenses = models.DecimalField(default=0, blank=True, null=True,
                                   max_digits=10, decimal_places=2)
    income = models.DecimalField(default=0, blank=True, null=True,
                                 max_digits=10, decimal_places=2)
    amount_income = models.DecimalField(default=0, blank=True, null=True,
                                        max_digits=10, decimal_places=2)
    amount_expenses = models.DecimalField(default=0, blank=True, null=True,
                                          max_digits=10, decimal_places=2)
    expenses_type = models.CharField(max_length=25, default='',
                                     choices=constants.EXPENSES_TYPE)
    income_type = models.CharField(max_length=25, default='',
                                   choices=constants.INCOME_TYPE)

    date = models.DateField(null=True)
    timestamp = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
