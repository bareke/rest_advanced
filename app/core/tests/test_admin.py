from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        user = get_user_model()
        self.admin_user = user.objects.create_superuser(
            email='admin@example.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = user.objects.create_user(
            email='user@example.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_create_user_page(self):
        """Test taht the create user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
