from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

from newspaper.models import Redactor, Topic, Newspaper

@login_required
def main_page(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
    }

    return render(request, "newspaper/index.html", context=context)


