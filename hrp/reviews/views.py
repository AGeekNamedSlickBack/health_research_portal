"""Reviews app views."""
from django.views.generic import CreateView, ListView

from .models import Review


class ReviewList(ListView):
    """A list of reviews."""

    queryset = Review.objects.order_by('-pub_date')
    context_object_name = 'review_list'


class ReviewCreateView(CreateView):
    """Create the review."""

    model = Review
    fields = ['rating', 'comment']
