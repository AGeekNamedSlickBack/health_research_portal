"""Researches app urls."""
from django.urls import path

from . import views

app_name = "researches"
urlpatterns = [
    path("", views.Index.as_view(), name="index",),
    path("cancer/", views.CancerTemplateView.as_view(), name="cancer",),
    path(
        "discussions/<int:pk>",
        views.DiscussionCreateView.as_view(),
        name="discussions",
    ),
    path(
        "discussions/replies_to_discussions/<int:pk>",
        views.DiscussionReplyCreateView.as_view(),
        name="replies_to_discussions",
    ),
    path(
        "recommend/<int:pk>/",
        views.RecommendsRedirectView.as_view(),
        name="recommends",
    ),
    path(
        "<int:pk>/", views.ResearchDetailView.as_view(), name="research-detail"
    ),
    path(
        "reviews/<int:pk>", views.ReviewCreateView.as_view(), name="reviews",
    ),
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
