import argparse
import requests
import bs4
import re
import json
from pathlib import Path

ROOT = "https://montrealgazette.com/"

def get_page(url, name):
    path = Path(f"data/{name}.html")
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

    if not path.exists():
        r = requests.get(url, headers=header)
        with open(path, 'w') as f:
            f.write(r.text)

    with open(path) as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description='Collect trending articles from the Montreal Gazette')
    parser.add_argument('--output', '-o', help='Output file name')
    args = parser.parse_args()

    out = args.output

    # Main page
    main = get_page("https://montrealgazette.com/category/news/", "Home")
    main_soup = bs4.BeautifulSoup(main, 'html.parser')

    trending_page = main_soup.find('ol', class_='list-widget__content list-unstyled').find_all('li')
    trending = []

    for i, article in enumerate(trending_page):
        link = article.find('a', class_='article-card__link').get('href')
        page = get_page(ROOT + link, f"Trending_{i}")
        page_soup = bs4.BeautifulSoup(page, 'html.parser')

        # Retrieve stuff
        div = page_soup.find('div', class_='article-header__detail')
        title = div.find('h1', id='articleTitle').text.strip()
        pub = div.find('span', class_='published-date__since').text.strip().split("Published ")[1]
        author = div.find(class_=re.compile('published-by__author')).text.strip()
        blurb = div.find('p', class_='article-subtitle').text.strip()

        d = {
            "title": title,
            "publication_date": pub,
            "author": author,
            "blurb": blurb,
        }

        trending.append(d)

    with open(f"data/{out}", 'w') as f:
        f.write(json.dumps(trending))
        
if __name__ == '__main__':
    main()
