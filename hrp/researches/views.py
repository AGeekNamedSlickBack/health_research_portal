"""Research views."""
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .filters import ResearchFilter
from .models import Research


class Index(TemplateView):
    """Landing page."""

    template_name = "index.html"


class CancerListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(category="cancer")
    context_object_name = "cancer_researches"
    template_name = "researches/cancer.html"
    paginate_by = 10


class MalariaListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(category="malaria")
    context_object_name = "malaria_researches"
    template_name = "researches/malaria.html"
    paginate_by = 10


def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})
