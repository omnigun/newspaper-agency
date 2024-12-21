from django.urls import path
from newspaper.views import (
    main_page,
    TopicListView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorExpirienceUpdateView,
    RedactorDeleteView,
    NewspaperListView,
    NewspaperDetailView)


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
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "redactors/create/",
         RedactorCreateView.as_view(),
        name="redactor-create"),
    path(
        "redactors/<int:pk>/delete/",
         RedactorDeleteView.as_view(),
        name="redactor-delete"),
    path("redactors/<int:pk>/expirience/",
         RedactorExpirienceUpdateView.as_view(), name="redactor-update"),

    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
]