from django.test import SimpleTestCase
from django.urls import resolve
from django.urls import reverse
from tracker.views import home, register
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_password_reset_url(self):
        url = reverse('password_reset')
        self.assertEquals(resolve(url).func.view_class,
                          auth_views.PasswordResetView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
