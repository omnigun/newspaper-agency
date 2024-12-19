from django.urls import path
from newspaper.views import (
    main_page,
    TopicListView,
    RedactorListView,
    NewspaperListView)


app_name = "newspaper"
urlpatterns = [
    path("", main_page, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list",
    ),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
]