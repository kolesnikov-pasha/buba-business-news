import json
from news_parsing.news_parser import tinkoff_url_to_id, consultant_url_to_id, klerk_url_to_id


def add_news_ids(filename):
    with open(filename, "r") as f:
        news_items = json.load(f)
    new_news_items = []
    for news_item in news_items:
        if news_item["source_domain"] == "journal.tinkoff.ru" and "id" not in news_item.keys():
            news_item["id"] = tinkoff_url_to_id(news_item["url"])
        if news_item["source_domain"] == "www.consultant.ru" and "id" not in news_item.keys():
            news_item["id"] = consultant_url_to_id(news_item["url"])
        if news_item["source_domain"] == "www.klerk.ru" and "id" not in news_item.keys():
            news_item["id"] = klerk_url_to_id(news_item["url"])
        new_news_items.append(news_item)
    with open(filename, "w") as f:
        json.dump(new_news_items, f, ensure_ascii=False)

