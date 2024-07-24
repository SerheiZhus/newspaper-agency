from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator
)
from django import forms
from newspaper.models import (
    Redactor,
    Newspaper,
    Topic,
)


class RedactorCreationForm(UserCreationForm):
    EXPERIENCE = 100
    years_of_experience = forms.CharField(
        required=True,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(EXPERIENCE),
        ]
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "years_of_experience",
        )


class RedactorExperienceUpdateForm(forms.ModelForm):
    EXPERIENCE = 100  # years
    years_of_experience = forms.CharField(
        required=True,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(EXPERIENCE),
        ]
    )

    class Meta:
        model = Redactor
        fields = ["years_of_experience"]


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperUpdateForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date"]


class RedactorSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={

                "placeholder": "Search by username"
            }
        )
    )


class TopicSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by topic"
            }
        )
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by newspaper"
            }
        )
    )
