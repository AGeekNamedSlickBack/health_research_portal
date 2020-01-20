"""Test fixtures."""
import pytest
from model_bakery import baker

from hrp.researches.models import Research
from hrp.reviews.models import Review
from django.test import Client

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
        url='http://urlyauongo.com',
        title='Kitu flani researched',
        scraped_date='2020-1-19',
    )


@pytest.fixture
def review(research):
    """Review."""
    return baker.make(
        Review,
        research=research,
        pub_date='2020-1-20',
        username='ule researcher',
        comment='Hii piece ni kali bana',
        rating='4',
    )
