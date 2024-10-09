from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AuthPagesTests(TestCase):
    def test_sign_up_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'UsersApp/signup.html')
        post_response = self.client.post(reverse('signup'), 
                                     {'username': 'Tester',
                                      'email': 'testing@gmail.com',
                                      'age': 69,
                                      'password1': 'testingpassword',
                                      'password2': 'testingpassword'})
        self.assertEqual(post_response.status_code, 302)
        user = get_user_model().objects.get(pk=1)
        self.assertEqual(user.username, 'Tester')