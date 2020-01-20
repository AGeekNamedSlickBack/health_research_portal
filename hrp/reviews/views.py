"""Reviews app views."""
from django.views.generic import ListView

from .models import Review


class ReviewList(ListView):
    """A list of reviews."""

    queryset = Review.objects.order_by('-pub_date')
    context_object_name = 'review_list'
