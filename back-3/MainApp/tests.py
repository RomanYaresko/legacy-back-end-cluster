from urllib import request
from django.test import TestCase, SimpleTestCase

class SimpleTest(SimpleTestCase):

    def test_home_status(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)


    def test_about_status(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)

    