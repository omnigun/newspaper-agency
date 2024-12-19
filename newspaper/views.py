from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from newspaper.models import Redactor, Topic, Newspaper

@login_required
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
    context_object_name = "topic_list"
    template_name = "newspaper/topic_list.html"
    extra_context = {"page_name_topic_list": True}
    paginate_by = 5


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/redactor_list.html"
    extra_context = {"page_name_redactor_list": True}
    paginate_by = 5


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_list.html"
    extra_context = {"page_name_newspaper_list": True}
    paginate_by = 5