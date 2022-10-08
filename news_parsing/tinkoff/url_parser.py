import bs4 as bs
import requests

from news_parser import NewsParser


class TinkoffParser(NewsParser):
    def __init__(self):
        super().__init__()
        self.parser_version = 1

    @staticmethod
    def url_to_id(url):
        return url[len("https://journal.tinkoff.ru/news/"):-1]


    @staticmethod
    def parse_all_pages_urls(base_url):
        pages = list(range(1, 51))
        urls = []
        for page in pages:
            urls += TinkoffParser.parse_page_urls(base_url, f"flows/goskontrol/page/{page}/")
        return urls


    @staticmethod
    def parse_page_urls(base_url, news_page_url):
        page = bs.BeautifulSoup(TinkoffParser.load_url(base_url + news_page_url), "html.parser")
        urls = []
        for item in page.find_all("div", attrs={"class": "card--LxPHF"}):
            href = item.find("a", attrs={"class": "link--xmoGM"})["href"]
            urls.append(base_url + href[1:])
        return urls
