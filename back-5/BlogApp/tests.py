from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import *

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='Tester', email='testing@gmail.com', password='testing0485')
        self.post = Post.objects.create(author=self.user, title='title', text='body body')

    def test_post(self):
        post = self.post
        self.assertEqual(str(post), post.title)
        self.assertEqual(post.get_absolute_url(), '/post/1/')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'title')
        self.assertEqual(post.text, 'body body')


    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApp/home.html')
        self.assertContains(response, 'title')


    def test_detail_post(self):
        response = self.client.get('/post/1/')
        wrong_response = self.client.get('/post/-1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(wrong_response.status_code, 404)
        self.assertTemplateUsed(response, 'BlogApp/post.html')
        self.assertContains(response, 'title')

    
    def test_create_new_post(self):
        response = self.client.post(reverse('new_post'), {'author': self.user, 'title': 'testing title', 'text': 'testing text'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testing title')


    def test_update_post(self):
        response = self.client.post(reverse('update_post', args='1'), {'title': 'update title', 'text': 'update text'})
        self.assertEqual(response.status_code, 302)


    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args='1'))
        self.assertEqual(response.status_code, 302)