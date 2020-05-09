"""Add a form for review checklist."""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Review, Discussion, DiscussionReply


class CustomUserCreationForm(UserCreationForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email", "first_name", "last_name")
        help_texts = {
            "username": None,
            "email": None,
        }
        labels = {
            "username": "",
            "email": "",
            "first_name": "",
            "last_name": "",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
        }


class CustomUserChangeForm(UserChangeForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email", "first_name", "last_name")
        labels = {
            "username": "",
            "email": "",
            "first_name": "",
            "last_name": "",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
        }


class ReviewForm(forms.ModelForm):
    """Create a checklist type of form."""

    class Meta:
        """Meta class."""

        model = Review
        fields = ["checklist"]
        widgets = {
            "selected_checklist": forms.CheckboxSelectMultiple,
        }


class DiscussionForm(forms.ModelForm):
    """Discussion form."""

    class Meta:
        """Meta class."""

        model = Discussion
        fields = ["discussion"]
        labels = {"discussion": ""}
        widgets = {
            "discussion": forms.Textarea(
                attrs={"placeholder": "Write your response..."}
            )
        }


class ReplyForm(forms.ModelForm):
    """Discussion form."""

    class Meta:
        """Meta class."""

        model = DiscussionReply
        fields = ["reply"]
        labels = {"reply": ""}
        widgets = {
            "reply": forms.Textarea(
                attrs={"placeholder": "Write your response..."}
            )
        }
