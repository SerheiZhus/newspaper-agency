from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="password123",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
            years_of_experience=5
        )

    def test_redactor_year_of_experience(self) -> None:
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_year_of_experience_first_name_last_name(self) -> None:
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.redactor.first_name)
        self.assertContains(res, self.redactor.last_name)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_year_of_experience_listed(self) -> None:
        url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)






