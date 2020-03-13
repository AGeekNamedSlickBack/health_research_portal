"""Test research models."""
import pytest

pytestmark = pytest.mark.django_db


def test_research_model(research):
    """Test research."""
    assert research.url == "http://urlyauongo.com"
    assert research.title == "Kitu flani researched"
    assert research.scraped_date == "2020-1-19"
    assert research.category == "malaria"
    assert research.keyword == "malaria_plasmodium"


def test_research_str_representation(research):
    """Test title string rep."""
    assert (
        str(research) == "Kitu flani researched - malaria - malaria_plasmodium"
    )


def test_discussions(discussion, research):
    """Test discussions."""
    assert discussion.research == research
    assert discussion.discussion == "Ni ya malaria"


def test_discussion_str_rep(discussion):
    """Test string representation."""
    assert str(discussion) == "Ni ya malaria"


def test_replies(research, discussion, reply):
    """Test discussions."""
    assert reply.discussion == discussion
    assert reply.reply == "Hapana ni ya cancer"


def test_replies_str_rep(reply):
    """Test string representation."""
    assert str(reply) == "Ni ya malaria - Hapana ni ya cancer"


def test_recommends(recommends, research):
    """Test recommends."""
    assert recommends.research == research


def test_recommends_str(recommends, research):
    """Test recommends string representation."""
    assert str(recommends) == "Kitu flani researched - 0"


def test_review_checklist(review_checklist):
    """Test creation of a review checklist."""
    assert review_checklist.create_checklist == "The research is well done"


def test_review_checklist_str(review_checklist):
    """Test review checklist string rep."""
    assert str(review_checklist) == "The research is well done"


def test_research_is_reviewed(research, review):
    """Test that a research has been reviewed."""
    assert review.research == research


def test_review_str(review):
    """Test review str rep."""
    assert str(review) == "Kitu flani researched"
