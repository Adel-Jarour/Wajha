from django.test import TestCase
from unittest.mock import patch
from scrapers.models import GrantSource, ScrapedGrant
from scrapers.scraper_scripts.opportunity_desk_scraper import OpportunityDeskScraper


class ScraperTestCase(TestCase):
    def setUp(self):
        # Clear state
        ScrapedGrant.objects.all().delete()
        GrantSource.objects.all().delete()

    @patch('requests.get')
    def test_opportunity_desk_scraper(self, mock_get):
        # Mock HTML structure representing an article post
        mock_html = """
        <html>
            <body>
                <article>
                    <h2 class="entry-title"><a href="https://opportunitydesk.org/test-scholarship/">Test Scholarship 2026</a></h2>
                    <div class="entry-summary">
                        <p>This is a description of the test scholarship. Deadline: August 12, 2026.</p>
                    </div>
                    <time datetime="2026-06-25T12:00:00Z"></time>
                    <span class="cat-links"><a href="#">Fellowships</a></span>
                </article>
            </body>
        </html>
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_html

        scraper = OpportunityDeskScraper()
        grants = scraper.scrape()

        # Assert correct parser extraction
        self.assertEqual(len(grants), 1)
        self.assertEqual(grants[0]['title'], 'Test Scholarship 2026')
        self.assertEqual(grants[0]['url'], 'https://opportunitydesk.org/test-scholarship/')
        self.assertEqual(grants[0]['deadline'], 'August 12, 2026')
        self.assertEqual(grants[0]['category'], 'Fellowships')

        # Assert correct database creation
        scraper.run()
        self.assertEqual(ScrapedGrant.objects.count(), 1)
        scraped_obj = ScrapedGrant.objects.first()
        self.assertEqual(scraped_obj.raw_title, 'Test Scholarship 2026')
        self.assertEqual(scraped_obj.status, 'pending')

