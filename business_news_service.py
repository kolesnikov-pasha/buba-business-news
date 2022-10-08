import json
from tqdm import tqdm
from google.cloud import storage


def upload_parsed_json(filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket("buba_news_data")
    with open(filename) as f:
        news_items = json.load(f)
        for news_item in tqdm(news_items):
            blob = bucket.blob(news_item["source_domain"] + "/" + news_item["id"])
            blob.upload_from_string(json.dumps(news_item, ensure_ascii=False))


upload_parsed_json("parsed_news.json")
