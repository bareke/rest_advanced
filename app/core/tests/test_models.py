from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating an new user with an email is sucessfull"""
        email = 'test@example.com'
        password = 'test'
        user = get_user_model()
        user = user.objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EXAMPLE.COM'
        password = 'test'
        user = get_user_model()
        user = user.objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            user = get_user_model()
            user.objects.create_user(email=None, password='test')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = 'test@example.com'
        password = 'test'
        user = get_user_model()
        user.objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
