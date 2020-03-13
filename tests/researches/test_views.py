"""Test research views."""
import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_index_view():
    """Test the research index view."""
    client = Client()
    url = reverse("research:index")
    response = client.get(url)

    assert response.status_code == 200


def test_cancer_template_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:cancer")
    response = client.get(url)

    assert response.status_code == 200


def test_discussion_view(research):
    """Test the research list view."""
    client = Client()
    url = reverse("research:discussions", args=(research.id,))
    response = client.get(url)

    assert response.status_code == 302


# def test_reply_view(research, discussion):
#     """Test the research list view."""
#     client = Client()
#     url = reverse("research:discussions", args=(discussion.id,))
#     response = client.get(url)

#     assert response.status_code == 200


def test_cancer_diagnosis_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:cancer_diagnosis")
    response = client.get(url)

    assert response.status_code == 200


def test_cancer_treatment_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:cancer_treatment")
    response = client.get(url)

    assert response.status_code == 200


def test_cancer_location_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:cancer_location")
    response = client.get(url)

    assert response.status_code == 200


def test_malaria_template_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:malaria")
    response = client.get(url)

    assert response.status_code == 200


def test_malaria_diagnosis_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:malaria_diagnosis")
    response = client.get(url)

    assert response.status_code == 200


def test_malaria_treatment_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:malaria_treatment")
    response = client.get(url)

    assert response.status_code == 200


def test_malaria_location_list_view():
    """Test the research list view."""
    client = Client()
    url = reverse("research:malaria_location")
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
