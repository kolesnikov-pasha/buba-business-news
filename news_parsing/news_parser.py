from newsplease import NewsPlease
import requests


class NewsParser:
    def __init__(self):
        self.parser_version = 0

    @staticmethod
    def load_url(url):
        return requests.get(url).content


    @staticmethod
    def parse_all_pages_urls(base_url):
        raise NotImplementedError()


    @staticmethod
    def parse_page_urls(base_url, news_page_url):
        raise NotImplementedError()


    @staticmethod
    def url_to_id(url):
        raise NotImplementedError()


    def __finish_parsing__(self, article):
        article["id"] = self.url_to_id(article["url"])
        article["parser_version"] = self.parser_version


    def parse_news(self, url):
        article = NewsPlease.from_url(url).get_dict()
        self.__finish_parsing__(article)
        article["date_publish"] = str(article["date_publish"]) if article["date_publish"] is not None else None
        article["date_download"] = str(article["date_download"]) if article["date_download"] is not None else None
        article["date_modify"] = str(article["date_modify"]) if article["date_modify"] is not None else None
        return article