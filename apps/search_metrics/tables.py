import django_tables2 as tables

from apps.search_metrics.models import SearchMetric


class SearchMetricsTable(tables.Table):
    class Meta:
        model = SearchMetric

    @classmethod
    def render_paginated_table(cls, request):
        table = cls(data=SearchMetric.objects.all())
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return table
