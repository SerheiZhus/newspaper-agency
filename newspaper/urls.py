from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics_list/", TopicListView.as_view(), name="topics-list"),
    path("newspaper_list/", NewspaperListView.as_view(), name="newspapers-list"),
    path("redactor_list/", RedactorListView.as_view(), name="redactors-list"),


]

app_name = "newspaper"
