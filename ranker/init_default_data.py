from google.cloud import storage
import json
from tqdm import tqdm


DEFAULT_USERS = {
    "ceo": {"type": "ceo", "user_id": "GsdgjnAwt325gn39v8h2t49nb24n254afdsbjn294b0q", "viewed": [], "clicked": []},
    "accountant": {"type": "accountant", "user_id": "1tVsgwr4ty2gv308hagh8VBNH4ygve9hrbw89v24q530", "viewed": [], "clicked": []}
}


def create_default_users():
    storage_client = storage.Client()
    bucket = storage_client.bucket("buba_news_data")
    for blob in tqdm(bucket.list_blobs()):
        news_id = blob.name
        DEFAULT_USERS["ceo"]["viewed"].append(news_id)
        DEFAULT_USERS["accountant"]["viewed"].append(news_id)
        if news_id.startswith("www.consultant.ru"):
            DEFAULT_USERS["ceo"]["clicked"].append(news_id)
            DEFAULT_USERS["accountant"]["clicked"].append(news_id)
        elif news_id.startswith("www.klerk.ru"):
            DEFAULT_USERS["accountant"]["clicked"].append(news_id)
        elif news_id.startswith("journal.tinkoff.ru"):
            DEFAULT_USERS["ceo"]["clicked"].append(news_id)
    with open("ranker/data/user_data.json", "w") as f:
        json.dump(DEFAULT_USERS, f)


create_default_users()
