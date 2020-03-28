"""Researches app urls."""
from django.urls import path

from . import views

app_name = "researches"
urlpatterns = [
    path("", views.Index.as_view(), name="index",),
    path("signup/", views.SignUp.as_view(), name="signup"),
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
        "my_recommends/",
        views.ReccomendedReasearchListView.as_view(),
        name="my_recommends",
    ),
    path(
        "<int:pk>/", views.ResearchDetailView.as_view(), name="research-detail"
    ),
    path(
        "reviews/<int:pk>", views.ReviewCreateView.as_view(), name="reviews",
    ),
    path("search/", views.Search.as_view(), name="search",),
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
    path("cholera/", views.CholeraTemplateView.as_view(), name="cholera",),
    path(
        "cholera/treatment/",
        views.CholeraTreatmentListView.as_view(),
        name="cholera_treatment",
    ),
    path("typhoid/", views.TyphoidTemplateView.as_view(), name="typhoid",),
    path(
        "typhoid/treatment/",
        views.TyphoidTreatmentListView.as_view(),
        name="typhoid_treatment",
    ),
    path(
        "typhoid/location/",
        views.TyphoidLocationListView.as_view(),
        name="typhoid_location",
    ),
    path("TB/", views.TBTemplateView.as_view(), name="TB",),
    path(
        "TB/treatment/",
        views.TBTreatmentListView.as_view(),
        name="TB_treatment",
    ),
    path("measles/", views.MeaslesTemplateView.as_view(), name="measles",),
    path(
        "measles/location/",
        views.MeaslesLocationListView.as_view(),
        name="measles_location",
    ),
    path("diabetes/", views.DiabetesTemplateView.as_view(), name="diabetes",),
    path(
        "diabetes/diagnosis/",
        views.DiabetesDiagnosisListView.as_view(),
        name="diabetes_diagnosis",
    ),
    path(
        "diabetes/treatment/",
        views.DiabetesTreatmentListView.as_view(),
        name="diabetes_treatment",
    ),
    path(
        "pneumonia/", views.PneumoniaTemplateView.as_view(), name="pneumonia",
    ),
    path(
        "pneumonia/diagnosis/",
        views.PneumoniaDiagnosisListView.as_view(),
        name="pneumonia_diagnosis",
    ),
    path(
        "malnutrition/",
        views.MalnutritionTemplateView.as_view(),
        name="malnutrition",
    ),
    path(
        "malnutrition/treatment/",
        views.MalnutritionTreatmentListView.as_view(),
        name="malnutrition_treatment",
    ),
    path(
        "malnutrition/location/",
        views.MalnutritionLocationListView.as_view(),
        name="malnutrition_location",
    ),
]
