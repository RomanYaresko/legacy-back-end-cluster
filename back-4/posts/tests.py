from turtle import pos
from django.test import TestCase
from django.urls import reverse
from .models import *

class MainPageModelTest(TestCase):

    def setUp(self):
        Post.objects.create(main_text = 'testing string')


    def test_post_create(self):
        post = Post.objects.get(id=1)
        testing_text = f'{post.main_text}'
        self.assertEqual(testing_text, 'testing string')

class MainPageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(main_text = 'testing string')


    def test_right_status_code(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)


    def test_right_template(self):
        response = self.client.get(reverse('posts'))
        self.assertTemplateUsed(response, 'posts/home.html')