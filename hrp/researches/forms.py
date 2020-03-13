"""Add a form for review checklist."""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Create a checklist type of form."""

    class Meta:
        """Meta class."""

        model = Review
        fields = ["checklist"]
        widgets = {
            "selected_checklist": forms.CheckboxSelectMultiple,
        }
