from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationViewTest(TestCase):
    def test_register_view_exists(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        
    def test_successful_registration(self):
        data = {
            'first_name': 'test',
            'email': 'test@example.com',
            'username': 'test01',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('register'), data, follow=True)
        self.assertRedirects(response, reverse('home'))
        
        # Check if the user is created
        self.assertTrue(User.objects.filter(username='test01').exists())

    def test_invalid_registration(self):
        data = {}
        response = self.client.post(reverse('register'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'All fields are required.')

    def test_existing_username(self):
        # Create a user with the same username as in test_successful_registration
        User.objects.create_user(username='test01', email='existing@example.com', password='existingpassword')

        data = {
            'first_name': 'test',
            'email': 'test@example.com',
            'username': 'test01',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('register'), data, follow=True)
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, 'A user with that username already exists.')
