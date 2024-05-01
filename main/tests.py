from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Favorite
from datetime import date

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
        self.assertRedirects(response, reverse('login'))
        
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

from django.contrib.auth import get_user_model

User = get_user_model()

class LoginViewTest(TestCase):
    def test_login_view_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_successful_login(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertRedirects(response, reverse('home'))

    def test_invalid_login(self):
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertContains(response, 'Invalid username or password.')
    def test_login_view_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_successful_login(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertRedirects(response, reverse('home'))

    def test_invalid_login(self):
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }
        response = self.client.post(reverse('login'), data, follow=True)
        self.assertContains(response, 'Invalid username or password.')

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Movie.objects.create(
            title='Test Movie',
            description='This is a test movie',
            director='Test Director',
            cast='Test Cast',
            genre='A',  # Assuming 'A' represents 'ACTION'
            category='TR',  # Assuming 'TR' represents 'TOP RATED'
            budget=1000000.00,
            release_date=date(2022, 1, 1),
            poster='http://example.com/poster.jpg'
        )

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.__str__(), 'Test Movie')

class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='testuser', password='12345')
        movie = Movie.objects.create(
            title='Test Movie',
            description='This is a test movie',
            director='Test Director',
            cast='Test Cast',
            genre='A',  # Assuming 'A' represents 'ACTION'
            category='TR',  # Assuming 'TR' represents 'TOP RATED'
            budget=1000000.00,
            release_date=date(2022, 1, 1),
            poster='http://example.com/poster.jpg'
        )
        Favorite.objects.create(user=user, movie=movie)

    def test_favorite_str(self):
        favorite = Favorite.objects.get(id=1)
        self.assertEqual(favorite.__str__(), 'testuser\'s favorite: Test Movie')
