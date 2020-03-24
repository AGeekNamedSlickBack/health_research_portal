"""Add a form for review checklist."""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Review


class CustomUserCreationForm(UserCreationForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email")


class ReviewForm(forms.ModelForm):
    """Create a checklist type of form."""

    class Meta:
        """Meta class."""

        model = Review
        fields = ["checklist"]
        widgets = {
            "selected_checklist": forms.CheckboxSelectMultiple,
        }
