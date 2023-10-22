import unittest
import unittest.mock as mock
from newscover.newsapi import fetch_latest_news
from parameterized import parameterized
from datetime import datetime, timedelta
from json import load

class TestNewsAPI(unittest.TestCase):

    @parameterized.expand([
        ([], "Keywords must be provided."),
        (["test", "test2", "test!"], "Keywords must be alphabetic.")
    ])
    def test_fetch_latest_news(self, news_keywords, error_message):
        with self.assertRaises(ValueError) as e:
            fetch_latest_news(api_key="", news_keywords=news_keywords, lookback_days=10)
        self.assertEqual(str(e.exception), error_message)

    @mock.patch('newscover.newsapi.NewsApiClient')
    def test_lookback_days(self, mock_api):
        
        with open("newscover/tests/test_lookback_days.json") as f:
            mock_api.return_value.get_everything.return_value = load(f)

        with self.assertRaises(ValueError) as e:
            fetch_latest_news(api_key="", news_keywords=["test"])

        self.assertEqual(str(e.exception), "News date is too old.")
