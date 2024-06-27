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
    TopicUpdateView,
    TopicDeleteView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorUpdateView,
    RedactorDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("topics_list/", TopicListView.as_view(), name="topics-list"),
    path("topics_list/<int:pk>/", TopicDetailView.as_view(), name="topics-detail"),
    path("topics_list/create/", TopicCreateView.as_view(), name="topics-create"),
    path("topics_list/<int:pk>/update/", TopicUpdateView.as_view(), name="topics-update"),
    path("topics_list/<int:pk>/delete/", TopicDeleteView.as_view(), name="topics-delete"),
    path("newspaper_list/", NewspaperListView.as_view(), name="newspapers-list"),
    path("newspaper_list/<int:pk>/", NewspaperDetailView.as_view(), name="newspapers-detail"),
    path("newspaper_list/create/", NewspaperCreateView.as_view(), name="newspapers-create"),
    path("newspaper_list/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspapers-update"),
    path("newspaper_list/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspapers-delete"),
    path("redactor_list/", RedactorListView.as_view(), name="redactors-list"),
    path("redactor_list/<int:pk>/", RedactorDetailView.as_view(), name="redactors-detail"),
    path("redactor_list/create/", RedactorCreateView.as_view(), name="redactors-create"),
    path("redactor_list/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactors-update"),
    path("redactor_list/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactors-delete"),


]

app_name = "newspaper"
