from django.contrib.messages import get_messages
from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from .consts import TasksConst
from .models import Label, Status


class StatusTest(TestCase):

    fixtures = ['data.json']

    def setUp(self):
        cache.clear()
        self.status_id = 7
        self.test_name = 'совсем зависло'
        self.exist_name = 'в работе'
        self.user_data = {'username': 'happylarry', 'password': '123'}
        self.status_data = {'name': self.test_name}
        self.exists_status_data = {'name': self.exist_name}

    def test_status_list(self):
        response = self.client.get(reverse('tasks:status_list'))
        self.assertEqual(response.status_code, 302)
        self.client.login(**self.user_data)
        response = self.client.get(reverse('tasks:status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.context)
        items = response.context["items"]
        self.assertTrue(len(items) > 0)

    def test_create(self):
        response = self.client.post(
            reverse('tasks:create_status'),
            self.status_data,
            follow=True
        )

        self.assertRedirects(response, reverse('login'))
        self.client.login(**self.user_data)

        response = self.client.post(
            reverse('tasks:create_status'),
            self.status_data,
            follow=True
        )

        self.assertRedirects(response, reverse('tasks:status_list'))

        self.assertTrue(Status.objects.filter(name=self.test_name).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.status_succ_create)

        response = self.client.post(
            reverse('tasks:create_status'),
            self.exists_status_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, TasksConst.status_exist)

    def test_update(self):

        url = reverse('tasks:update_status', kwargs={'pk': self.status_id})

        response = self.client.post(url, self.status_data, follow=True)

        self.assertRedirects(response, reverse('login'))
        self.client.login(**self.user_data)
        
        response = self.client.post(url, self.status_data, follow=True)

        self.assertRedirects(response, reverse('tasks:status_list'))

        status = Status.objects.filter(pk=self.status_id)[0]
        self.assertEqual(status.name, self.test_name)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.status_succ_update)

    def test_delete(self):

        url = reverse('tasks:delete_status', kwargs={'pk': self.status_id})

        response = self.client.post(url, follow=True)

        self.assertRedirects(response, reverse('login'))

        self.client.login(**self.user_data)

        response = self.client.post(url, follow=True)

        self.assertRedirects(response, reverse('tasks:status_list'))

        status = list(Status.objects.filter(pk=self.status_id))
        self.assertEqual(len(status), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.status_succ_delete)

        ## еще нужен тест на удаление того, что есть в задачах

        # response = self.client.post(
        #     reverse('tasks:create_status'),
        #     self.exists_status_data,
        #     follow=True
        # )

        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, TasksConst.status_exist)


class LabelTest(TestCase):

    fixtures = ['data.json']

    def setUp(self):
        cache.clear()
        self.label_id = 7
        self.test_name = 'тестовая метка'
        self.exist_name = 'метка3'
        self.user_data = {'username': 'happylarry', 'password': '123'}
        self.label_data = {'name': self.test_name}
        self.exists_label_data = {'name': self.exist_name}

    def test_label_list(self):
        response = self.client.get(reverse('tasks:label_list'))
        self.assertEqual(response.status_code, 302)
        self.client.login(**self.user_data)
        response = self.client.get(reverse('tasks:label_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.context)
        items = response.context["items"]
        self.assertTrue(len(items) > 0)

    def test_create(self):
        response = self.client.post(
            reverse('tasks:create_label'),
            self.label_data,
            follow=True
        )

        self.assertRedirects(response, reverse('login'))
        self.client.login(**self.user_data)

        response = self.client.post(
            reverse('tasks:create_label'),
            self.label_data,
            follow=True
        )

        self.assertRedirects(response, reverse('tasks:label_list'))

        self.assertTrue(Label.objects.filter(name=self.test_name).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.label_succ_create)

        response = self.client.post(
            reverse('tasks:create_label'),
            self.exists_label_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, TasksConst.label_exist)

    def test_update(self):

        url = reverse('tasks:update_label', kwargs={'pk': self.label_id})

        response = self.client.post(url, self.label_data, follow=True)

        self.assertRedirects(response, reverse('login'))
        self.client.login(**self.user_data)
        
        response = self.client.post(url, self.label_data, follow=True)

        self.assertRedirects(response, reverse('tasks:label_list'))

        label = Label.objects.filter(pk=self.label_id)[0]
        self.assertEqual(label.name, self.test_name)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.label_succ_update)

    def test_delete(self):

        url = reverse('tasks:delete_label', kwargs={'pk': self.label_id})

        response = self.client.post(url, follow=True)

        self.assertRedirects(response, reverse('login'))

        self.client.login(**self.user_data)

        response = self.client.post(url, follow=True)

        self.assertRedirects(response, reverse('tasks:label_list'))

        label = list(Label.objects.filter(pk=self.label_id))
        self.assertEqual(len(label), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), TasksConst.label_succ_delete)

        ## еще нужен тест на удаление того, что есть в задачах

        # response = self.client.post(
        #     reverse('tasks:create_status'),
        #     self.exists_status_data,
        #     follow=True
        # )

        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, TasksConst.status_exist)

