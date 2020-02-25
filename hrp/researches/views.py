"""Research views."""
from django.shortcuts import render
from django.views.generic import ListView

from .filters import ResearchFilter
from .models import Research


class ResearchListView(ListView):
    """List view of spareparts."""

    queryset = Research.objects.all()
    context_object_name = "researches"
    paginate_by = 10


def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})
