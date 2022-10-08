import bs4 as bs
import requests

from news_parser import NewsParser


class KlerkParser(NewsParser):
    def __init__(self):
        super().__init__()
        self.parser_version = 1

    @staticmethod
    def parse_all_pages_urls(base_url):
        pages = list(range(1, 50))
        urls = []
        for page in pages:
            urls += KlerkParser.parse_page_urls(base_url, f"page/{page}/")
        return urls


    @staticmethod
    def parse_page_urls(base_url, news_page_url):
        page = bs.BeautifulSoup(KlerkParser.load_url(base_url + news_page_url), "html.parser")
        urls = []
        for item in page.find_all("article"):
            href = item.find("a", attrs={"class": ["feed-item-link__check-article", "feed-item__link"]})["href"]
            urls.append(base_url + href[len("/buh/news/"):])
        return urls

    
    @staticmethod
    def url_to_id(url):
        return url[len("https://www.klerk.ru/buh/news/"):-1]
