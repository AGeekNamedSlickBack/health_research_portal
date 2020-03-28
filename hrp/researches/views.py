"""Research views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
)

from .forms import CustomUserCreationForm, ReviewForm
from .models import Discussion, DiscussionReply, Recommends, Research, Review


class Index(TemplateView):
    """Landing page."""

    template_name = "index.html"


class SignUp(CreateView):
    """Sign up view for users."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("research:index")
    template_name = "registration/signup.html"


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    """Add discussions."""

    model = Discussion
    fields = ["discussion"]
    template_name = "discussions.html"
    login_url = "login"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        """Override form valid to add user and research."""
        form.instance.created_by = self.request.user
        form.instance.research_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect here."""
        return reverse_lazy(
            "research:discussions", kwargs={"pk": self.kwargs.get("pk")}
        )

    def get_context_data(self, **kwargs):
        """List discussions of a research."""
        research = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["discussions_list"] = Discussion.objects.filter(
            research=research
        ).order_by("-created_on")
        context["discussed_research"] = Research.objects.get(pk=research)
        return context


class DiscussionReplyCreateView(LoginRequiredMixin, CreateView):
    """Add discussions."""

    model = DiscussionReply
    fields = ["reply"]
    template_name = "replies_to_discussions.html"
    login_url = "login"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        """Override form valid to add user and research."""
        form.instance.created_by = self.request.user
        form.instance.discussion_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect here."""
        return reverse_lazy(
            "research:replies_to_discussions",
            kwargs={"pk": self.kwargs.get("pk")},
        )

    def get_context_data(self, **kwargs):
        """List discussions of a research."""
        discussion = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["replies_to_discussions"] = DiscussionReply.objects.filter(
            discussion=discussion
        ).order_by("-created_on")
        context["replied_on_discussion"] = Discussion.objects.get(
            pk=discussion
        )
        return context


class RecommendsRedirectView(LoginRequiredMixin, RedirectView):
    """Add recommends to a research."""

    permanent = False
    query_string = False
    pattern_name = "research:research-detail"

    def get_redirect_url(self, *args, **kwargs):
        """Redirect to the discussion page."""
        research = get_object_or_404(Research, pk=kwargs["pk"])
        user = self.request.user
        recommended_research, _ = Recommends.objects.get_or_create(
            research_id=research
        )
        if user.is_authenticated:
            if user in recommended_research.recommends.all():
                recommended_research.recommends.remove(user)
            else:
                recommended_research.recommends.add(user)
        return super().get_redirect_url(*args, **kwargs)


class ReccomendedReasearchListView(LoginRequiredMixin, ListView):
    """Get a list of all recommended researches."""

    template_name = "my_recommends.html"
    context_object_name = "recommended_research"
    paginate_by = 10

    def get_queryset(self):
        """Filter by user."""
        return Research.objects.filter(
            researches__recommends=self.request.user
        )


class Search(ListView):
    """Search view for spareparts."""

    model = Research
    template_name = "search.html"
    context_object_name = "searches"
    paginate_by = 10

    def get_queryset(self):
        """Get filtered queryset."""
        query = self.request.GET.get("q")
        return Research.objects.filter(
            Q(title__icontains=query)
            | Q(category__icontains=query)
            | Q(keyword__icontains=query)
        )


class ResearchDetailView(DetailView):
    """Add detail views for the researches."""

    model = Research
    template_name = "research_details.html"

    def get_context_data(self, **kwargs):
        """Define context data."""
        context = super().get_context_data(**kwargs)
        research = self.kwargs.get("pk")
        recommended_research, _ = Recommends.objects.get_or_create(
            research_id=research
        )
        context["recommender"] = self.request.user
        context["recommenders"] = recommended_research.recommends.all()
        context["recommends_count"] = recommended_research.recommends.count()
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """Create a review for a recommended research."""

    model = Review
    template_name = "reviews.html"
    login_url = "login"
    redirect_field_name = "redirect_to"
    form_class = ReviewForm

    def form_valid(self, form):
        """Override form valid to add user and research."""
        form.instance.created_by = self.request.user
        form.instance.research_id = self.kwargs.get("pk")
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect the reviews page."""
        return reverse_lazy(
            "research:research-detail", kwargs={"pk": self.kwargs.get("pk")}
        )

    def get_context_data(self, **kwargs):
        """Get the research to be reviewed."""
        research = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["reviewed_research"] = Research.objects.get(pk=research)
        return context


class CancerTemplateView(TemplateView):
    """Cancer page template view."""

    template_name = "researches/cancer.html"


class CancerDiagnosisListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cancer:diagnosis")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cancer_diagnosis"
    template_name = "researches/cancer_diagnosis.html"
    paginate_by = 10


class CancerTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cancer:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cancer_treatment"
    template_name = "researches/cancer_treatment.html"
    paginate_by = 10


class CancerLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cancer:county")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cancer_location"
    template_name = "researches/cancer_location.html"
    paginate_by = 10


class MalariaTemplateView(TemplateView):
    """Malaria page template view."""

    template_name = "researches/malaria.html"


class MalariaDiagnosisListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(keyword="malaria:plasmodium").annotate(
        research_count=Count("researches__recommends")
    ).order_by("-research_count") | Research.objects.filter(
        keyword="malaria:diagnosis"
    ).annotate(
        research_count=Count("researches__recommends")
    ).order_by(
        "-research_count"
    )
    context_object_name = "malaria_diagnosis"
    template_name = "researches/malaria_diagnosis.html"
    paginate_by = 10


class MalariaTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malaria:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malaria_treatment"
    template_name = "researches/malaria_treatment.html"
    paginate_by = 10


class MalariaLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malaria:county")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malaria_location"
    template_name = "researches/malaria_location.html"
    paginate_by = 10


class CholeraTemplateView(TemplateView):
    """Cholera page template view."""

    template_name = "researches/cholera.html"


class CholeraTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cholera:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cholera_treatment"
    template_name = "researches/cholera_treatment.html"
    paginate_by = 10


class TyphoidTemplateView(TemplateView):
    """Typhoid page template view."""

    template_name = "researches/typhoid.html"


class TyphoidTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="typhoid:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "typhoid_treatment"
    template_name = "researches/typhoid_treatment.html"
    paginate_by = 10


class TyphoidLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="typhoid:county")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "typhoid_location"
    template_name = "researches/typhoid_location.html"
    paginate_by = 10


class TBTemplateView(TemplateView):
    """TB page template view."""

    template_name = "researches/TB.html"


class TBTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="tuberculosis:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "TB_treatment"
    template_name = "researches/TB_treatment.html"
    paginate_by = 10


class MeaslesTemplateView(TemplateView):
    """Measles page template view."""

    template_name = "researches/measles.html"


class MeaslesLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="measles:county")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "measles_location"
    template_name = "researches/measles_location.html"
    paginate_by = 10


class DiabetesTemplateView(TemplateView):
    """Diabetes page template view."""

    template_name = "researches/diabetes.html"


class DiabetesDiagnosisListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="diabetes+mellitus:diagnosis")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "diabetes_diagnosis"
    template_name = "researches/diabetes_diagnosis.html"
    paginate_by = 10


class DiabetesTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="diabetes+mellitus:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "diabetes_treatment"
    template_name = "researches/diabetes_treatment.html"
    paginate_by = 10


class PneumoniaTemplateView(TemplateView):
    """Pneumonia page template view."""

    template_name = "researches/pneumonia.html"


class PneumoniaDiagnosisListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="pneumonia:diagnosis")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "pneumonia_diagnosis"
    template_name = "researches/pneumonia_diagnosis.html"
    paginate_by = 10


class MalnutritionTemplateView(TemplateView):
    """Malnutrition page template view."""

    template_name = "researches/malnutrition.html"


class MalnutritionTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malnutrition:treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malnutrition_treatment"
    template_name = "researches/malnutrition_treatment.html"
    paginate_by = 10


class MalnutritionLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malnutrition:county")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malnutrition_location"
    template_name = "researches/malnutrition_location.html"
    paginate_by = 10
