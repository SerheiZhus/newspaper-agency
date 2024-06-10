from django.contrib.auth.models import AbstractUser
from django.db import models

from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        max_length=100,
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ("username", )

    def __str__(self) -> str:
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    class Meta:
        ordering = ("title", )

    def __str__(self) -> str:
        return f"{self.title} - {self.topic} - {self.published_date}"
