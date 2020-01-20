"""Reviews urlconf."""
from django.conf.urls import url

from . import views

app_name = 'reviews'
urlpatterns = [
    url(regex=r'^$', view=views.ReviewList.as_view(), name='list'),
]
