from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_info', views.add_info, name='add_info'),
    path('add_income', views.add_income, name='add_income'),
    path('add_expenses', views.add_expenses, name='add_expenses'),
]
