from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.mybnb.business_logic import get_opt_params
from apps.mybnb.models import Home
from apps.mybnb.search_index import search_index


@require_http_methods(["POST", "GET"])
def search(request):
    
    context, query_dict = {}, {}
    # use template partial for htmx requests
    template_name = "mybnb/search.html"
    if request.htmx:
        template_name = "mybnb/htmx/gallery.html"
    else:
        context.update(Home.objects.get_filter_attributes())
    
    # fetch and format search query parameters
    query_dict = request.GET if request.method == "GET" else request.POST
    opt_params = get_opt_params(query_dict)
    query = query_dict.get("query", None)
    
    # fetch results from the index and add them to the context
    results = search_index.search(query=query, opt_params=opt_params)
    context.update(
        {
            "homes": results["hits"],
            "total": results["nbHits"],
            "processing_time": results["processingTimeMs"],
            "next_offset": opt_params.get("offset", 0) + 20  # used for infinite scroll
        }
    )
    return render(request, template_name, context)


def preview_home(request, doc_id):
    home = search_index.get_document(doc_id)
    template_name = "mybnb/htmx/preview.html"
    return render(request, template_name, {"home": home})
