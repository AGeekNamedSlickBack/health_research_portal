"""Filter researches."""
import django_filters

from .models import Research


class ResearchFilter(django_filters.FilterSet):
    """Create the filter set for researches."""

    class Meta:
        """Meta data."""

        model = Research
        fields = ["category"]
