import bs4 as bs
import requests


def load_url(url):
    return requests.get(url).content


def parse_tinkoff_all(base_url):
    pages = list(range(1, 2))
    urls = []
    for page in pages:
        urls += parse_tinkoff(base_url, f"flows/goskontrol/page/{page}/")
    return urls


def parse_tinkoff(base_url, news_page_url):
    page = bs.BeautifulSoup(load_url(base_url + news_page_url), "html.parser")
    urls = []
    for item in page.find_all("div", attrs={"class": "card--LxPHF"}):
        href = item.find("a", attrs={"class": "link--xmoGM"})["href"]
        urls.append(base_url + href[1:])
    return urls
