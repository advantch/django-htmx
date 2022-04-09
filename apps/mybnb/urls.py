from django.urls import path
from django.views.generic import RedirectView

from .views import search, preview_home

app_name = "mybnb"
urlpatterns = [
    path("", RedirectView("mybnb:search")),
    path("search/", search, name="search"),
    path("preview_home/<str:doc_id>", preview_home, name="preview"),
]
