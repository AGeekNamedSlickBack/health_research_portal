"""Research models."""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Research(models.Model):
    """Create the model for research."""

    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    scraped_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=250)
    keyword = models.CharField(max_length=100)

    def __str__(self):
        """Rep title into a human readable form."""
        return "{} - {} - {}".format(self.title, self.category, self.keyword)


class Discussion(models.Model):
    """Create discussions for a research."""

    research = models.ForeignKey(
        Research, on_delete=models.CASCADE, related_name="discussions"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    discussion = models.TextField()

    class Meta:
        """Meta class."""

        ordering = ["-created_on"]

    def __str__(self):
        """Human readable form."""
        return self.discussion


class DiscussionReply(models.Model):
    """User can reply to a discussion."""

    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="replies"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()

    class Meta:
        """Meta class."""

        ordering = ["-created_on"]
        verbose_name = "DiscussionReplie"

    def __str__(self):
        """Human readable form."""
        return f"{self.discussion} - {self.reply}"


class Recommends(models.Model):
    """A research is ranked on its number of recommends."""

    research = models.ForeignKey(
        Research, on_delete=models.CASCADE, related_name="researches"
    )
    recommends = models.ManyToManyField(
        User, blank=True, related_name="recommends"
    )

    class Meta:
        """Model meta options."""

        verbose_name = "Recommend"

    def __str__(self):
        """Human readable form."""
        count = self.recommends.count()
        return f"{self.research.title} - {count}"


class ReviewChecklist(models.Model):
    """Create a checklist for review."""

    create_checklist = models.CharField(max_length=255)

    def __str__(self):
        """Human readable form."""
        return self.create_checklist


class Review(models.Model):
    """User check the checklist."""

    research = models.ForeignKey(
        Research, on_delete=models.CASCADE, related_name="research_to_review"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    checklist = models.ManyToManyField(ReviewChecklist)

    def __str__(self):
        """Human readable form."""
        return self.research.title
