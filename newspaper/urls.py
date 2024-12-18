from django.urls import path
from newspaper.views import (
    main_page,
    TopicListView)


app_name = "newspaper"
urlpatterns = [
    path("", main_page, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
]