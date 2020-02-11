"""Test fixtures."""
import pytest
from model_bakery import baker

from hrp.researches.models import Research

pytestmark = pytest.mark.django_db


@pytest.fixture
def research():
    """Research."""
    return baker.make(
        Research,
        url="http://urlyauongo.com",
        title="Kitu flani researched",
        scraped_date="2020-1-19",
        category="malaria"
    )
