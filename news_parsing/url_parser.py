import json
from consultant_plus.url_parser import ConsultantParser
from klerk.url_parser import KlerkParser
from tinkoff.url_parser import TinkoffParser
from tqdm import tqdm
from google.cloud import storage


__PARSERS__ = {
    "consultant_plus": ConsultantParser(),
    "klerk": KlerkParser(),
    "tinkoff": TinkoffParser()
}


storage_client = storage.Client()
bucket = storage_client.bucket("buba_news_data")


def get_blob_name(source, domen, url):
    id = __PARSERS__[source].url_to_id(url)
    return domen + "/" + id


def check_should_parse_url(source, domen, url):
    blob = bucket.blob(get_blob_name(source, domen, url))
    return not blob.exists()


def get_loaded_parser_version(source, domen, url):
    blob = bucket.blob(get_blob_name(source, domen, url))
    news_item = json.loads(blob.download_as_string())
    return news_item["parser_version"] if "parser_version" in news_item else 0


def upload_update(source, domen, url, news_item):
    blob = bucket.blob(get_blob_name(source, domen, url))
    blob.upload_from_string(json.dumps(news_item, ensure_ascii=False))



def parse_all_sources():
    sources = json.load(open("news_parsing/sources.json"))
    for source in sources["sources"]:
        if source["name"] in __PARSERS__:
            parser = __PARSERS__[source["name"]]
            print(f"Start parsing {source['name'].upper()}")
            urls = parser.parse_all_pages_urls(source["base_url"])
            for url in tqdm(urls):
                if check_should_parse_url(source["name"], source["domen"], url) or \
                    get_loaded_parser_version(source["name"], source["domen"], url) < parser.parser_version:
                    news_item = parser.parse_news(url)
                    upload_update(source["name"], source["domen"], url, news_item)


parse_all_sources()
