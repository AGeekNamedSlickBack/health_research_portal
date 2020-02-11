"""Test research models."""
import pytest

pytestmark = pytest.mark.django_db


def test_research_model(research):
    """Test research."""
    assert research.url == "http://urlyauongo.com"
    assert research.title == "Kitu flani researched"
    assert research.scraped_date == "2020-1-19"
    assert research.category == "malaria"


def test_research_str_representation(research):
    """Test title string rep."""
    assert str(research) == "Kitu flani researched - malaria"
