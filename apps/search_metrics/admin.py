from django.contrib import admin

from apps.search_metrics.models import SearchMetric


@admin.register(SearchMetric)
class SearchMetricsAdmin(admin.ModelAdmin):
    pass
