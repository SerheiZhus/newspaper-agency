from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    NewspaperListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics_list/", TopicListView.as_view(), name="topics-list"),
    path("newspaper_list/", NewspaperListView.as_view(), name="newspapers-list"),


]

app_name = "newspaper"
