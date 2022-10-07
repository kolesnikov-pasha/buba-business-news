import bs4 as bs
import requests


def load_url(url):
    return requests.get(url).content


def parse_consultant_plus_all(base_url):
    years = [2022]
    months = {
        2020: list(range(1, 13)),
        2021: list(range(1, 13)),
        2022: list(range(10, 11))
    }
    for year in years:
        for month in months[year]:
            print(parse_consultant_plus(base_url, f"legalnews/chronomap/{year}/{month}"))


def parse_consultant_plus(base_url, news_page_url):
    page = bs.BeautifulSoup(load_url(base_url + news_page_url), "html.parser")
    listing = page.find("div", attrs={"class": "archive-month__listing"})
    urls = []
    for item in listing.find_all("div", attrs={"class": "archive-month__item"}):
        href = item.find("a", attrs={"class": "archive-month__item-title"})["href"]
        urls.append(base_url + href[1:])
    return urls