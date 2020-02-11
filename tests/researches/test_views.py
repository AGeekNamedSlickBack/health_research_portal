"""Test research views."""
import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_research_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:list")
    response = client.get(url)

    assert response.status_code == 200


def test_research_search_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:search")
    response = client.get(url)

    assert response.status_code == 200
