import bs4 as bs
import requests
from news_parser import NewsParser
from datetime import datetime


class ConsultantParser(NewsParser):
    def __init__(self):
        super().__init__()
        self.parser_version = 2


    @staticmethod
    def parse_all_pages_urls(base_url):
        years = [2022, 2021, 2020]
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


    def __finish_parsing__(self, article):
        super().__finish_parsing__(article)
        page_content = NewsParser.load_url(article["url"])
        news_page = bs.BeautifulSoup(page_content, "html.parser")
        months = ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
        info = news_page.find("div", attrs={"class": "news-page__date"}).string.split()
        day = int(info[0])
        month = 1
        for i in range(12):
            if info[1].startswith(months[i]):
                month = i + 1
                break
        year = int(info[2])
        article["date_publish"] = datetime(year, month, day)
        print(article["date_publish"])
