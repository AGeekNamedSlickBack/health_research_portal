"""Create a custom 'python3 manage.py scrape' command."""
from django.core.management.base import BaseCommand

from hrp.common.util.scraper import scraper


class Command(BaseCommand):
    """Create a custom 'scrape' command."""

    help = "Scrapes research"

    def handle(self, *args, **options):
        """Scrape command."""
        scraper()

        self.stdout.write(self.style.SUCCESS("Successfully scraped."))
