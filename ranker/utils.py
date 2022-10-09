from google.cloud import storage
import json
import requests


__cache__ = {}


def __get_news_embed__(news_id):
    if news_id in __cache__:
        return __cache__[news_id]
    storage_client = storage.Client()
    bucket = storage_client.bucket("buba_news_data")
    news = json.loads(bucket.blob(news_id).download_as_string())
    response = requests.post("http://127.0.0.1:8000/", json={
        "maintext": news["maintext"],
        "title": news["title"]
    })
    print(response.json())
