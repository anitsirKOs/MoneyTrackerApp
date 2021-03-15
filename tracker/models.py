from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

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

    timestamp = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return str(self.user)
