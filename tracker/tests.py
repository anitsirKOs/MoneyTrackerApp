from django.test import SimpleTestCase
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.urls import reverse
from .views import home
from django.contrib.auth import views as auth_views

# Create your tests here.


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


class TrackerTestCase(TestCase):

    def setUp(self):
        super(TrackerTestCase, self).setUp()
        self.client = Client()

    def test_add_income_POST_returns200(self):
        response = self.client.post(
            '/add_info/',
            {'income_type': 'income_type', 'date': 'date',
             'amount_income': 'amount_income'},
        )
        self.assertEquals(response.status_code, 200)

    def test_add_expenses_POST_returns302(self):
        response = self.client.post(
            '/add_expenses/',
            {'expenses_type': 'expenses_type', 'date': 'date',
             'amount_expenses': 'amount_expenses'},
        )
        self.assertEquals(response.status_code, 302)
