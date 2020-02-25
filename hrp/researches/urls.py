"""Researches app urls."""
from django.urls import path

from . import views

app_name = "researches"
urlpatterns = [
    path("", views.Index.as_view(), name="index",),
    path("cancer/", views.CancerListView.as_view(), name="cancer",),
    path("malaria/", views.MalariaListView.as_view(), name="malaria",),
    path("search/", views.research_search, name="search"),
]
