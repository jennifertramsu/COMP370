from newsapi import NewsApiClient
from datetime import datetime, timedelta

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    """
    Fetches latest news from NewsAPI and returns a Python list of english news articles (represented as dictionaries) 
    containing those news keywords and published within the last <lookback_days>.

    Parameters
    ----------
    param api_key: str
        API key for News API

    param news_keywords: list(str)
        Keywords to search for

    param lookback_days: int (default: 10)
        Number of days to look back for news

    Returns
    -------
    :return: list(dict)
        List of news articles
    """
    # Input validation
    # 1) news_keywords cannot be empty
    if len(news_keywords) == 0:
        raise ValueError("Keywords must be provided.")
    
    # 2) all keywords must only contain alphabetic characters
    if not all(keyword.isalpha() for keyword in news_keywords):
        raise ValueError("Keywords must be alphabetic.")

    # Initialize News API
    newsapi = NewsApiClient(api_key=api_key)

    # Extracting news keywords
    news_keywords_str = ' AND '.join(news_keywords)

    # Extracting data range
    to_date = datetime.now().date()
    from_date = to_date - timedelta(days=lookback_days)

    # Converting dates to ISO format
    to_date = to_date.isoformat()
    from_date = from_date.isoformat()

    # Fetching news
    news = newsapi.get_everything(q=news_keywords_str, language="en", from_param=from_date, to=to_date)

    return news['articles']