"""Research views."""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    RedirectView,
    TemplateView,
    DetailView,
)

from .filters import ResearchFilter
from .models import Discussion, DiscussionReply, Recommends, Research, Review
from .forms import ReviewForm
from django.db.models import Count


class Index(TemplateView):
    """Landing page."""

    template_name = "index.html"


class SignUp(CreateView):
    """Sign up view for users."""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
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
        Research.objects.filter(keyword="cancer_diagnosis")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cancer_diagnosis"
    template_name = "researches/cancer_diagnosis.html"
    paginate_by = 10


class CancerTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cancer_treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "cancer_treatment"
    template_name = "researches/cancer_treatment.html"
    paginate_by = 10


class CancerLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="cancer_county")
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

    queryset = (
        Research.objects.filter(keyword="malaria_Plasmodium")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malaria_diagnosis"
    template_name = "researches/malaria_diagnosis.html"
    paginate_by = 10


class MalariaTreatmentListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malaria_treatment")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malaria_treatment"
    template_name = "researches/malaria_treatment.html"
    paginate_by = 10


class MalariaLocationListView(ListView):
    """List view of researches."""

    queryset = (
        Research.objects.filter(keyword="malaria_County")
        .annotate(research_count=Count("researches__recommends"))
        .order_by("-research_count")
    )
    context_object_name = "malaria_location"
    template_name = "researches/malaria_location.html"
    paginate_by = 10


def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})
