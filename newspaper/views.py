from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count

from newspaper.models import Redactor, Topic, Newspaper
from newspaper.forms import (
    RedactorCreationForm,
    RedactorExperienceForm,
    NewspaperForm)


def main_page(request):
    """View function for the home page of the site."""
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()

    context = {
        "page_name_index": True,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
    }
    return render(request, "newspaper/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    queryset = Topic.objects.all().annotate(news=Count('newspaper__pk'))
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    extra_context = {"page_name_topic_list": True}
    paginate_by = 5


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers").annotate(news=Count('newspapers__pk'))
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    extra_context = {"page_name_redactor_list": True}
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    context_object_name = "redactor"
    template_name = "newspaper/redactor_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newspapers = Newspaper.objects.prefetch_related("publishers").filter(publishers__pk=self.object.id)
        context["newspapers"] = newspapers
        return context


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorExperienceForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.all().select_related("topic")
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
    extra_context = {"page_name_newspaper_list": True}
    paginate_by = 5


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    context_object_name = "newspaper"
    template_name = "newspaper/newspaper_detail.html"
    extra_context = {"page_name_newspaper_detail": True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publishers = Redactor.objects.all().filter(newspapers__pk=self.object.id)
        context["publishers"] = publishers
        return context


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")