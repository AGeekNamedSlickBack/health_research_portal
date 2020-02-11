"""Research views."""
from django.views.generic import ListView

from .models import Research


class ResearchListView(ListView):
    """List view of spareparts."""

    queryset = Research.objects.all()
    context_object_name = "researches"
