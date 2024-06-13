from django.urls import path

from newspaper.views import index, TopicListview

urlpatterns = {
    path("", index, name="index"),
    path("topics/", TopicListview.as_view(), name="topics"),

}

app_name = "newspaper"
