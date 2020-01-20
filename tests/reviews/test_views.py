"""Test review views."""
import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_review_list_view(review, client):
    """Test review list view."""
    url = reverse('reviews:list')
    response = client.get(url)

    assert response.status_code == 200
