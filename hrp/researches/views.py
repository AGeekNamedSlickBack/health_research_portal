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


# class LikeView(RedirectView):
#     """Like view for researches."""

#     def get_redirect_url(self, *args, **kwargs):
#         """Get the redirect url."""
#         research = get_object_or_404(Research, pk=kwargs['pk'])
#         user = self.request.user
#         research.likes.add(user)
#         return super().get_redirect_url(*args, **kwargs)


class CancerListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(category="cancer")
    context_object_name = "cancer_researches"
    template_name = "researches/cancer.html"
    paginate_by = 10


class MalariaListView(ListView):
    """List view of researches."""

    queryset = Research.objects.filter(category="malaria")
    context_object_name = "malaria_researches"
    template_name = "researches/malaria.html"
    paginate_by = 10


def research_search(request):
    """Filter view."""
    f = ResearchFilter(request.GET, queryset=Research.objects.all())
    return render(request, "researches/search.html", {"filter": f})
