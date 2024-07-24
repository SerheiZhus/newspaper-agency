from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse
from newspaper.forms import NewspaperSearchForm
from newspaper.models import Newspaper, Topic
from newspaper.views import NewspaperListView

NEWSPAPER_URL = reverse("newspaper:newspapers-list")


class PublicRedactorTest(TestCase):

    def test_login_required(self) -> None:
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateNewspaperTest(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.redactor = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test",
            last_name="test",
            years_of_experience=1,

            )
        self.topic = Topic.objects.create(
            name="test3"
        )
        self.publisher = get_user_model().objects.create_user(
            username="test4"
        )
        self.newspaper = Newspaper.objects.create(
            title="test1",
            content="test2",
            published_date="2021-01-01",

        )
        self.newspaper.topic.set([self.topic])
        self.newspaper.publishers.set([self.publisher])
        self.client.force_login(self.redactor)

    def test_retrieve_newspaper(self) -> None:
        res = self.client.get(NEWSPAPER_URL)
        newspaper = Newspaper.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["object_list"]),
            list(newspaper),
        )
        self.assertEqual(
            res.context_data["paginator"].num_pages,
            1
        )
        self.assertTemplateUsed(
            res,
            "newspaper/newspaper_list.html",
        )

    def test_viw_context_data(self) -> None:
        response = self.client.get(NEWSPAPER_URL)
        self.assertTrue("search_form" in response.context)
        self.assertIsInstance(
            response.context["search_form"],
            NewspaperSearchForm
        )

    def test_view_queryset(self) -> None:
        request = self.factory.get(NEWSPAPER_URL, {"title": "test"})
        request.user = self.redactor
        view = NewspaperListView()
        view.request = request
        queryset = view.get_queryset()
        self.assertEqual(len(queryset), 1)
        self.assertEqual(
            queryset[0].title,
            "test1"
        )
        self.assertEqual(
            queryset[0].content,
            "test2"
        )
        self.assertEqual(
            queryset[0].topic.first().name,
            "test3"
        )
        self.assertEqual(
            queryset[0].publishers.first().username,
            "test4"
        )

        self.assertEqual(
            queryset[0].published_date.strftime("%Y-%m-%d"),
            "2021-01-01"
        )
