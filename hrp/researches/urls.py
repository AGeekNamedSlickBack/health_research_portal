"""Researches app urls."""
from django.urls import path

from . import views

app_name = "researches"
urlpatterns = [
    path("", views.Index.as_view(), name="index",),
    path("cancer/", views.CancerTemplateView.as_view(), name="cancer",),
    path(
        "cancer/diagnosis/",
        views.CancerDiagnosisListView.as_view(),
        name="cancer_diagnosis",
    ),
    path(
        "cancer/treatment/",
        views.CancerTreatmentListView.as_view(),
        name="cancer_treatment",
    ),
    path(
        "cancer/location/",
        views.CancerLocationListView.as_view(),
        name="cancer_location",
    ),
    path("malaria/", views.MalariaTemplateView.as_view(), name="malaria",),
    path(
        "malaria/diagnosis/",
        views.MalariaDiagnosisListView.as_view(),
        name="malaria_diagnosis",
    ),
    path(
        "malaria/treatment/",
        views.MalariaTreatmentListView.as_view(),
        name="malaria_treatment",
    ),
    path(
        "malaria/location/",
        views.MalariaLocationListView.as_view(),
        name="malaria_location",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("search/", views.research_search, name="search"),
]
