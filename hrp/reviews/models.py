"""Review models."""
from django.db import models
from django.utils import timezone

from hrp.researches.models import Research


class Review(models.Model):
    """Create the fields for review."""

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    research = models.ForeignKey(Research, on_delete=models.PROTECT)
    pub_date = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)  # Better rating

    def __str__(self):
        """Str representation."""
        return "Research: {} - Rated: {}".format(self.research, self.rating)

    # TODO get the average of all ratings.
