from django.shortcuts import render
from django.views import generic
from newspaper.models import (
    Redactor,
    Topic,
    Newspaper,
)


def index(request) -> render:

    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()
    num_newspaper = Newspaper.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactor": num_redactor,
        "num_topic": num_topic,
        "num_newspaper": num_newspaper,
        "num_visits": num_visits + 1,
    }

    return render(
        request,
        "newspaper/index.html",
        context=context
    )


class TopicListView(generic.ListView):
    model = Topic


class NewspaperListView(generic.ListView):
    model = Newspaper


class RedactorListView(generic.ListView):
    model = Redactor
