from django.urls import re_path, path

from apps.search_metrics.views import search_metrics_view, seed_db_view, clear_db_view

app_name = "search_metrics"
urlpatterns = [
    re_path(r"^(?:page-(?P<page_number>\d+)/)?$", search_metrics_view, name="search-metrics-table"),
    path("seed-db/", seed_db_view, name="seed-db"),
    path("clear-db/", clear_db_view, name="clear-db")
]
