from django.urls import path

from newspaper.views import (
    index,
    TopicListView,
    TopicDetailView,
    NewspaperListView,
    RedactorListView,
    NewspaperDetailView,
    RedactorDetailView,
    TopicCreateView,
    NewspaperCreateView,
    RedactorCreateView,

)

urlpatterns = [
    path("", index, name="index"),
    path("topics_list/", TopicListView.as_view(), name="topics-list"),
    path("topics_list/<int:pk>", TopicDetailView.as_view(), name="topics-detail"),
    path("topics_list/create/", TopicCreateView.as_view(), name="topics-create"),
    path("newspaper_list/", NewspaperListView.as_view(), name="newspapers-list"),
    path("newspaper_list/<int:pk>", NewspaperDetailView.as_view(), name="newspapers-detail"),
    path("newspaper_list/create/", NewspaperCreateView.as_view(), name="newspapers-create"),
    path("redactor_list/", RedactorListView.as_view(), name="redactors-list"),
    path("redactor_list/<int:pk>", RedactorDetailView.as_view(), name="redactors-detail"),
    path("redactor_list/create/", RedactorCreateView.as_view(), name="redactors-create")


]

app_name = "newspaper"
