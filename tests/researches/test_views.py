"""Test research views."""
import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_index_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:index")
    response = client.get(url)

    assert response.status_code == 200


def test_cancer_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:cancer")
    response = client.get(url)

    assert response.status_code == 200


def test_malaria_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:malaria")
    response = client.get(url)

    assert response.status_code == 200


def test_research_search_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:search")
    response = client.get(url)

    assert response.status_code == 200


def test_signup_view():
    """Test the signup view."""
    client = Client()
    url = reverse("research:signup")
    response = client.get(url)

    assert response.status_code == 200
