"""Test review models."""
import pytest

pytestmark = pytest.mark.django_db


def test_review_models(review, research):
    """Test the review models."""
    assert review.research == research
    assert review.pub_date == "2020-1-20"
    assert review.username == "ule researcher"
    assert review.comment == "Hii piece ni kali bana"
    assert review.rating == "4"


def test_review_str_representation(review):
    """Test review string representation."""
    assert (
        str(review) == "Research: Kitu flani researched - malaria - Rated: 4"
    )
