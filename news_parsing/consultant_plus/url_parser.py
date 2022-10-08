import bs4 as bs
import requests
from news_parser import NewsParser


class ConsultantParser(NewsParser):
    def __init__(self):
        super().__init__()
        self.parser_version = 1


    @staticmethod
    def parse_all_pages_urls(base_url):
        years = [2022]
        months = {
            2020: list(range(1, 13)),
            2021: list(range(1, 13)),
            2022: list(range(6, 11))
        }
        urls = []
        for year in years:
            for month in months[year]:
                urls += ConsultantParser.parse_page_urls(base_url, f"legalnews/chronomap/{year}/{month}")
        return urls


    @staticmethod
    def parse_page_urls(base_url, news_page_url):
        page = bs.BeautifulSoup(ConsultantParser.load_url(base_url + news_page_url), "html.parser")
        listing = page.find("div", attrs={"class": "archive-month__listing"})
        urls = []
        for item in listing.find_all("div", attrs={"class": "archive-month__item"}):
            href = item.find("a", attrs={"class": "archive-month__item-title"})["href"]
            urls.append(base_url + href[1:])
        return urls

    
    @staticmethod
    def url_to_id(url):
        return url[len("http://www.consultant.ru/legalnews/"):-1]
