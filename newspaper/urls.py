from django.urls import path
from newspaper.views import main_page


app_name = "newspaper"
urlpatterns = [
    path("", main_page, name="index"),

]