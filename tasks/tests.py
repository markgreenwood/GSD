from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from tasks.views import home_page
from tasks.models import Task 

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

class TaskModelTest(TestCase):
    def test_saving_and_retrieving_tasks(self):
        first_task = Task()
        first_task.text = "The first (ever) task"
        first_task.save()

        second_task = Task()
        second_task.text = "Task the second"
        second_task.save()

        saved_tasks = Task.objects.all()
        self.assertEqual(saved_tasks.count(), 2)

        first_saved_task = saved_tasks[0]
        second_saved_task = saved_tasks[1]
        self.assertEqual(first_saved_task.text, 'The first (ever) task')
        self.assertEqual(second_saved_task.text, 'Task the second')
