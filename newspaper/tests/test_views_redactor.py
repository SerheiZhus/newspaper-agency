from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse
from newspaper.forms import RedactorSearchForm
from newspaper.models import Redactor
from newspaper.views import RedactorListView

REDACTOR_URL = reverse("newspaper:redactors-list")


class PublicRedctorTest(TestCase):

    def test_login_required(self) -> None:
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.redactor = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test",
            last_name="test",
            years_of_experience=1,

            )
        self.client.force_login(self.redactor)

    def test_retrieve_redactors(self) -> None:
        res = self.client.get(REDACTOR_URL)
        redactors = Redactor.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["object_list"]),
            list(redactors),
        )
        self.assertEqual(
            res.context_data["paginator"].num_pages,
            1
        )
        self.assertTemplateUsed(
            res,
            "newspaper/redactor_list.html",
        )

    def test_viw_context_data(self) -> None:
        response = self.client.get(REDACTOR_URL)
        self.assertTrue("search_form" in response.context)
        self.assertIsInstance(
            response.context["search_form"],
            RedactorSearchForm
        )

    def test_view_queryset(self) -> None:
        request = self.factory.get(REDACTOR_URL, {"username": "test1"})
        request.user = self.redactor
        view = RedactorListView()
        view.request = request
        queryset = view.get_queryset()
        self.assertEqual(len(queryset), 1)
        self.assertEqual(
            queryset[0].username,
            "test"
        )
        self.assertEqual(
            queryset[0].first_name,
            "test"
        )
        self.assertEqual(
            queryset[0].last_name,
            "test"
        )
        self.assertEqual(
            queryset[0].years_of_experience,
            1
        )
