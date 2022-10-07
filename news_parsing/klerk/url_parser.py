import bs4 as bs
import requests


def load_url(url):
    return requests.get(url).content


def parse_klerk_all(base_url):
    pages = list(range(1, 4))
    urls = []
    for page in pages:
        urls += parse_klerk(base_url, f"page/{page}/")
    return urls


def parse_klerk(base_url, news_page_url):
    page = bs.BeautifulSoup(load_url(base_url + news_page_url), "html.parser")
    urls = []
    for item in page.find_all("article"):
        href = item.find("a", attrs={"class": ["feed-item-link__check-article", "feed-item__link"]})["href"]
        urls.append(base_url + href[len("/buh/news/"):])
    return urls
