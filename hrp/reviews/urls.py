"""Reviews urlconf."""
from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', view=views.ReviewList.as_view(), name='list'),
    path('create/', view=views.ReviewCreateView.as_view(), name='create'),
]
