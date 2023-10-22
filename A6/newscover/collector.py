import argparse
from newscover.newsapi import fetch_latest_news
from json import load, dumps
from pathlib import Path

def main():
    # Initializating ArgumentParser
    parser = argparse.ArgumentParser(description='Fetch news articles from NewsAPI')

    parser.add_argument('-k', required=True, help='API key for NewsAPI')
    parser.add_argument('-b', required=False, help='Number of days to look back for news', default=10)
    parser.add_argument('-i', required=True, help='Input file name')
    parser.add_argument('-o', required=True, help='Output directory name')

    args = parser.parse_args()
    api_key = args.k
    lookback_days = int(args.b)
    input_file = args.i
    output_dir = Path(args.o)

    # Loading file
    with open(input_file) as f:
        data = load(f)

    # Check if output directory exists
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    
    # Fetching news
    for name in data.keys():
        news = fetch_latest_news(api_key=api_key, news_keywords=data[name], lookback_days=lookback_days)
        news = dumps(news)
        
        # Writing to file in output dir
        with open(output_dir / f'{name}.json', 'w') as f:
            f.write(news)

if __name__ == '__main__':
    main()