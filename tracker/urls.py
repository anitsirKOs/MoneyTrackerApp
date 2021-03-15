from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.show_start_page, name='index'),
    path('home/', views.home, name='home'),
    path('add_info/', views.add_info, name='add_info'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expenses/', views.add_expenses, name='add_expenses'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='registration/logout.html'),
         name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', views.view_profile, name='profile'),
    path('register/', views.register, name='register'),

]
