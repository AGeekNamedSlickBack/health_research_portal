"""Research views."""
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .filters import ResearchFilter
from .models import Research


class Index(TemplateView):
    """Landing page."""

    template_name = "index.html"


class SignUp(CreateView):
    """Sign up view for users."""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CancerTemplateView(TemplateView):
    """Cancer page template view."""

    template_name = "researches/cancer.html"


class CancerDiagnosisListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="cancer_diagnosis")
    context_object_name = "cancer_diagnosis"
    template_name = "researches/cancer_diagnosis.html"
    paginate_by = 10


class CancerTreatmentListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="cancer_treatment")
    context_object_name = "cancer_treatment"
    template_name = "researches/cancer_treatment.html"
    paginate_by = 10


class CancerLocationListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="cancer_county")
    context_object_name = "cancer_location"
    template_name = "researches/cancer_location.html"
    paginate_by = 10


class MalariaTemplateView(TemplateView):
    """Malaria page template view."""

    template_name = "researches/malaria.html"


class MalariaDiagnosisListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="malaria_Plasmodium")
    context_object_name = "malaria_diagnosis"
    template_name = "researches/malaria_diagnosis.html"
    paginate_by = 10


class MalariaTreatmentListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="malaria_treatment")
    context_object_name = "malaria_treatment"
    template_name = "researches/malaria_treatment.html"
    paginate_by = 10


class MalariaLocationListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="malaria_County")
    context_object_name = "malaria_location"
    template_name = "researches/malaria_location.html"
    paginate_by = 10

def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})
