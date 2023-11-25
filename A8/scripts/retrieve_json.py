import requests
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subreddit", "-s", help="Subreddit to scrape")
    parser.add_argument("--limit", "-l", help="Number of posts to scrape")
    parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    subreddit = args.subreddit
    limit = args.limit
    output = args.output

    url = "https://www.reddit.com/r/" + subreddit + "/new.json?limit=" + limit

    r = requests.get(url)
    data = r.json()

    print(data)

if __name__ == "__main__":
    main()