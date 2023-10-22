import unittest
from newscover.newsapi import fetch_latest_news
from parameterized import parameterized
from datetime import datetime, timedelta

class TestNewsAPI(unittest.TestCase):

    @parameterized.expand([
        ([], "Keywords must be provided."),
        (["test", "test2", "test!"], "Keywords must be alphabetic.")
    ])
    def test_fetch_latest_news(self, news_keywords, error_message):
        with self.assertRaises(ValueError) as e:
            fetch_latest_news(api_key="", news_keywords=news_keywords, lookback_days=10)
        self.assertEqual(str(e.exception), error_message)

    def test_lookback_days(self):
        news = fetch_latest_news(api_key="5ddf953964854e318559ff90282266c0", news_keywords=["test"], lookback_days=20)

        for n in news:
            date = n['publishedAt'].split('T')[0]
            date = datetime.strptime(date, '%Y-%m-%d').date()
            with self.subTest(date=date):
                self.assertGreaterEqual(date, datetime.now().date() - timedelta(days=20))
