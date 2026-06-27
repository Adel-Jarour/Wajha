"""
Registry of all active scrapers.
Add new scrapers here so the management command picks them up automatically.
"""
from .opportunity_desk_scraper import OpportunityDeskScraper

# All scrapers that will be run by `python manage.py run_scrapers`
ALL_SCRAPERS = [
    OpportunityDeskScraper,
    # Add more scrapers here as you build them:
    # from .chevening_scraper import CheveningScraper
    # ChevenningScraper,
]
