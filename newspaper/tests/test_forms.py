from django.contrib.auth import get_user_model
from django.test import TestCase
from newspaper.forms import (
    NewspaperForm,
    RedactorCreationForm,
    RedactorExperienceUpdateForm,
    RedactorSearchForm,
    TopicSearchForm,
    NewspaperSearchForm
)
from django import forms

from newspaper.models import Topic


class FormsTests(TestCase):

    def test_redactor_creation_form(self) -> None:
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "Test",
            "last_name": "User",
            "years_of_experience": "10",
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_newspaper_form(self) -> None:
        form = NewspaperForm(
            data={
                "title": "Test title",
                "content": "Test content",
                "published_date": "2021-01-01",
                "topic": [Topic.objects.create(
                    name="Test topic"
                )
                ],

                "publishers": [get_user_model().objects.create_user(
                    username="test_user"
                )
                ],
            }
        )
        self.assertTrue(form.is_valid())
        self.assertIsInstance(
            form.fields["publishers"],
            forms.ModelMultipleChoiceField
        )
        self.assertIsInstance(
            form.fields["publishers"].widget,
            forms.CheckboxSelectMultiple
        )
        self.assertIsInstance(
            form.fields["topic"],
            forms.ModelMultipleChoiceField
        )
        self.assertIsInstance(
            form.fields["topic"].widget,
            forms.CheckboxSelectMultiple
        )
        self.assertEqual(
            form.changed_data,
            form.changed_data
        )

    def test_redactor_experience_update_form(self) -> None:
        form = RedactorExperienceUpdateForm(
            data={
                "years_of_experience": "10"
            }
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data,
            {"years_of_experience": "10"}
        )


class SearchFormTests(TestCase):

    def test_search_form(self) -> None:
        form_redactor = RedactorSearchForm(
            data={"title": "test_user"}
        )
        form_topic = TopicSearchForm(
            data={"title": "test_topic"}
        )
        form_newspaper = NewspaperSearchForm(
            data={"title": "test_title"}
        )
        self.assertTrue(form_redactor.is_valid())
        self.assertTrue(form_topic.is_valid())
        self.assertTrue(form_newspaper.is_valid())
        self.assertEqual(
            form_redactor.cleaned_data,
            {"title": "test_user"}
        )
        self.assertEqual(
            form_topic.cleaned_data,
            {"title": "test_topic"}
        )
        self.assertEqual(
            form_newspaper.cleaned_data,
            {"title": "test_title"}
        )
