"""Researches app urls."""
from django.urls import path

from . import views

app_name = "researches"
urlpatterns = [
    path("", views.ResearchListView.as_view(), name="list",),
    path("search/", views.research_search, name="search"),
]
