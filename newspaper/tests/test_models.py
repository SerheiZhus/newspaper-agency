from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from newspaper.models import Topic, Redactor, Newspaper


class ModelsTestCase(TestCase):

    def test_topic_str(self) -> None:
        topic_str = Topic.objects.create(
            name="Test Topic"
        )
        self.assertEqual(
            str(topic_str),
            f"{topic_str.name}"
        )

    def test_redactor_str(self) -> None:
        redactor_str = Redactor.objects.create(
            username="Test Redactor"
        )
        self.assertEqual(
            str(redactor_str),
            f"{redactor_str.username}"
        )

    def test_newspaper_str(self) -> None:
        topic = Topic.objects.create(
            name="Test Topic"
        )
        publisher = get_user_model().objects.create_user(
            username="Test Publisher"
        )
        newspaper_str = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test Content",
            published_date="2021-01-01",

        )
        newspaper_str.topic.set([topic])
        newspaper_str.publishers.set([publisher])
        self.assertEqual(
            str(newspaper_str),
            f"{newspaper_str.title}"

        )

    def test_redactor_get_absolute_url(self):
        redactor = get_user_model().objects.create_user(
            username="Test Redactor",
            password="testpassword",
            years_of_experience=5,

        )
        expected_url = reverse(
            "newspaper:redactors-detail",
            kwargs={"pk": redactor.pk}
        )
        self.assertEqual(
            redactor.get_absolute_url(),
            expected_url
        )
