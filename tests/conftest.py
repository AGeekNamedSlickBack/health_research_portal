"""Test fixtures."""
import pytest
from model_bakery import baker

from hrp.researches.models import Research, ResearchCategory

pytestmark = pytest.mark.django_db


@pytest.fixture
def research():
    """Research."""
    return baker.make(
        Research,
        url="http://urlyauongo.com",
        title="Kitu flani researched",
        scraped_date="2020-1-19",
    )


@pytest.fixture
def research_category(research):
    """Research category."""
    return baker.make(ResearchCategory, research=research, category="malaria",)
