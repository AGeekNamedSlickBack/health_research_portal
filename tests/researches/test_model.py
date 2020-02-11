"""Test research models."""
import pytest

pytestmark = pytest.mark.django_db


def test_research_model(research):
    """Test research."""
    assert research.url == "http://urlyauongo.com"
    assert research.title == "Kitu flani researched"
    assert research.scraped_date == "2020-1-19"


def test_research_str_representation(research):
    """Test title string rep."""
    assert str(research) == "Kitu flani researched"


def test_research_category(research_category, research):
    """Test research category."""
    assert research_category.research == research
    assert research_category.category == "malaria"


def test_research_category_str_representation(research_category):
    """Test title string rep."""
    assert str(research_category) == "malaria"
