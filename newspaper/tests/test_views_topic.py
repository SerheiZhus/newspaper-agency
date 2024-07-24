from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse
from newspaper.forms import TopicSearchForm
from newspaper.models import Topic
from newspaper.views import TopicListView

TOPIC_URL = reverse("newspaper:topics-list")


class PublicTopicTest(TestCase):

    def test_login_required(self) -> None:
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.redactor = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )

        Topic.objects.create(
                name="test1",

            )
        self.client.force_login(self.redactor)

    def test_retrieve_topics(self) -> None:
        res = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["object_list"]),
            list(topics),
        )
        self.assertEqual(
            res.context_data["paginator"].num_pages,
            1
        )
        self.assertTemplateUsed(
            res,
            "newspaper/topic_list.html",
        )

    def test_viw_context_data(self) -> None:
        response = self.client.get(TOPIC_URL)
        self.assertTrue("search_form" in response.context)
        self.assertIsInstance(
            response.context["search_form"],
            TopicSearchForm
        )

    def test_view_queryset(self) -> None:
        request = self.factory.get(TOPIC_URL, {"name": "test1"})
        request.user = self.redactor
        view = TopicListView()
        view.request = request
        queryset = view.get_queryset()
        self.assertEqual(len(queryset), 1)
        self.assertEqual(
            queryset[0].name,
            "test1"
        )
