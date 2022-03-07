import django_tables2 as tables

from apps.search_metrics.models import SearchMetric


class SearchMetricsTable(tables.Table):
    class Meta:
        model = SearchMetric
