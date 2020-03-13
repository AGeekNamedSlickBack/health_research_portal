"""Test fixtures."""
import pytest
from django.test import Client
from model_bakery import baker

from hrp.researches.models import (
    Discussion,
    DiscussionReply,
    Recommends,
    Research,
    Review,
    ReviewChecklist,
)

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    """Test client."""
    return Client()


@pytest.fixture
def research():
    """Research."""
    return baker.make(
        Research,
        url="http://urlyauongo.com",
        title="Kitu flani researched",
        scraped_date="2020-1-19",
        category="malaria",
        keyword="malaria_plasmodium",
    )


@pytest.fixture
def discussion(research):
    """Return discussion."""
    return baker.make(
        Discussion,
        research=research,
        created_on="2020-12-1",
        discussion="Ni ya malaria",
    )


@pytest.fixture
def reply(research, discussion):
    """Return reply to discussion."""
    return baker.make(
        DiscussionReply,
        discussion=discussion,
        created_on="2020-12-1",
        reply="Hapana ni ya cancer",
    )


@pytest.fixture
def recommends(research):
    """Return recommends."""
    return baker.make(Recommends, research=research)


@pytest.fixture
def review_checklist():
    """Return a review checklist."""
    return baker.make(
        ReviewChecklist, create_checklist="The research is well done"
    )


@pytest.fixture
def review(review_checklist, research):
    """Return a review."""
    return baker.make(Review, research=research)
