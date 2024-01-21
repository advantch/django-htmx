import django_tables2 as tables

from apps.search_metrics.models import SearchMetric


class SearchMetricsTable(tables.Table):
    class Meta:
        model = SearchMetric

    @classmethod
    def render_paginated_table(cls, request):
        sort = request.GET.get("sort", None)
        objects = SearchMetric.objects.all()
        if sort:
            objects = objects.order_by(sort)
        table = cls(data=objects)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        return table
