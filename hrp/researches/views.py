"""Research views."""
from django.shortcuts import render
from django.views.generic import ListView

from .filters import ResearchFilter
from .models import Research
from .search import searching


class ResearchListView(ListView):
    """List view of spareparts."""

    queryset = Research.objects.all()
    context_object_name = "researches"
    paginate_by = 10


def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})


def search_index(request):
    """Search index view."""
    results = []
    title_term = ""
    category_term = ""
    if request.GET.get("title") and request.GET.get("category"):
        title_term = request.GET["title"]
        category_term = request.GET["category"]
    elif request.GET.get("title"):
        title_term = request.GET["category"]
    elif request.GET.get("category"):
        title_term = request.GET["category"]
    search_term = title_term or category_term
    results = searching(title=title_term, category=category_term)
    context = {
        "results": results,
        "count": len(results),
        "search_term": search_term,
    }
    return render(request, "researches/search.html", context)
