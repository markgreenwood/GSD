from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from tasks.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request=request) # passing request=request handles csrf_token in Django 1.9
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['task_text'] = 'A new task'

        response = home_page(request)

        self.assertIn('A new task', response.content.decode())
        expected_html = render_to_string('home.html', {'new_task_text': 'A new task'}, request=request)
        self.assertEqual(response.content.decode(), expected_html)
