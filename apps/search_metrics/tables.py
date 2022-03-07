import django_tables2 as tables

from apps.search_metrics.models import SearchMetric


class SearchMetricsTable(tables.Table):
    class Meta:
        model = SearchMetric
        row_attrs = {
            "data-id": lambda record: record.id,
            "hx-trigger": "click",
            "hx-target": "#record-preview",
        }
