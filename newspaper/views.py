from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import (
    RedactorCreationForm,
    NewspaperForm,
    RedactorSearchForm,
    TopicSearchForm,
    NewspaperSearchForm
)
from newspaper.models import (
    Redactor,
    Topic,
    Newspaper,
)


@login_required
def index(request) -> render:

    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()
    num_newspaper = Newspaper.objects.count()

    num_visits = request.session.get(
        "num_visits",
        0
    )
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


class TopicListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Topic
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = TopicSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return Topic.objects.filter(
                name__icontains=form.cleaned_data["title"]
            )
        return Topic.objects.all()


class TopicDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Topic


class TopicCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topics-list")
    template_name = "newspaper/topic_form.html"


class TopicUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topics-list")
    template_name = "newspaper/topic_form.html"


class TopicDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Topic
    success_url = reverse_lazy("newspaper:topics-list")
    template_name = "newspaper/topic_confirm_delete.html"


class NewspaperListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Newspaper
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        form = NewspaperSearchForm(self.request.GET)
        if form.is_valid():
            return Newspaper.objects.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return Newspaper.objects.all().prefetch_related("topic", "publishers")


class NewspaperDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Newspaper


class NewspaperCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    success_url = reverse_lazy("newspaper:newspapers-list")
    template_name = "newspaper/newspaper_form.html"
    form_class = NewspaperForm


class NewspaperUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspapers-list")
    template_name = "newspaper/newspaper_form.html"
    form_class = NewspaperForm


class NewspaperDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspapers-list")
    template_name = "newspaper/newspaper_confirm_delete.html"


class RedactorListView(
    LoginRequiredMixin,
    generic.ListView
):
    model = Redactor
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = RedactorSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return Redactor.objects.filter(
                username__icontains=form.cleaned_data["title"]
            )
        return Redactor.objects.all()


class RedactorDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    model = Redactor


class RedactorCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Redactor

    success_url = reverse_lazy("newspaper:redactors-list")
    template_name = "newspaper/redactor_form.html"
    form_class = RedactorCreationForm


class RedactorUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactors-list")
    template_name = "newspaper/redactor_form.html"
    form_class = RedactorCreationForm


class RedactorDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactors-list")
    template_name = "newspaper/redactor_confirm_delete.html"
