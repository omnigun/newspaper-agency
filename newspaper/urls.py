from django.urls import path
from newspaper.views import main_page


urlpatterns = [
    path("", main_page, name="index"),
]