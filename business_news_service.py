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


def download_parsed_json(filename):
    storage_client = storage.Client()
    bucket = storage_client.bucket("buba_news_data")
    news_items = []
    for blob in tqdm(list(bucket.list_blobs())):
        news_items.append(json.loads(blob.download_as_string()))
    with open(filename, "w") as f:
        json.dump(news_items, f)
