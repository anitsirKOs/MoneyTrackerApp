from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TrackerTestCase(TestCase):

    def setUp(self):
        super(TrackerTestCase, self).setUp()
        self.client = Client()
        self.index_url = reverse('index')
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        test_user = User.objects.create_user(username='user', password='1111')
        test_user.save()

    def test_add_income_POST_returns302(self):
        response = self.client.post(
            '/add_info/',
            {'income_type': 'income_type',
             'amount_income': 'amount_income'},
        )
        self.assertEqual(response.status_code, 302)

    def test_add_expenses_POST_returns302(self):
        response = self.client.post(
            '/add_info/',
            {'expenses_type': 'expenses_type',
             'amount_expenses': 'amount_expenses'},
        )
        self.assertEqual(response.status_code, 302)

    def test_show_start_page(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_income'))
        self.assertRedirects(response, '/login/?next=/add_income/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='user', password='1111')
        response = self.client.get(reverse('profile'))
        self.assertEqual(str(response.context['user']), 'user')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')
