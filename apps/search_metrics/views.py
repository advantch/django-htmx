from django.core.management import call_command
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.search_metrics.models import SearchMetric
from apps.search_metrics.tables import SearchMetricsTable


def search_metrics_view(request):
    
    # select correct template based on request
    template_name = "search_metrics/metrics.html"
    if request.htmx:
        template_name = "search_metrics/htmx/table.html"
        
    search_metrics_table = SearchMetricsTable(data=SearchMetric.objects.all())
    search_metrics_table.paginate(page=request.GET.get("page", 1), per_page=25)
    context = {"table": search_metrics_table}
    
    return render(request, template_name, context)


@require_http_methods(["POST"])
def seed_db_view(request):
    
    call_command("seed_db")
    template_name = "search_metrics/htmx/table.html"

    search_metrics_table = SearchMetricsTable(data=SearchMetric.objects.all())
    search_metrics_table.paginate(page=request.GET.get("page", 1), per_page=25)
    context = {"table": search_metrics_table}

    return render(request, template_name, context)


@require_http_methods(["DELETE"])
def clear_db_view(request):
    template_name = "search_metrics/htmx/table.html"
    
    SearchMetric.objects.all().delete()
    
    search_metrics_table = SearchMetricsTable(data=SearchMetric.objects.all())
    search_metrics_table.paginate(page=request.GET.get("page", 1), per_page=25)
    context = {"table": search_metrics_table}
    
    return render(request, template_name, context)
