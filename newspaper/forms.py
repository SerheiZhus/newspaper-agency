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
    Topic
)


class RedactorCreationForm(UserCreationForm):
    EXPERIENCE = 100  # years
    years_of_experience = forms.CharField(

        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(EXPERIENCE),
        ]
    )

    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "years_of_experience",
        )


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    published_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
