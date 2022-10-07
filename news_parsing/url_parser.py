import json
from news_parser import parse_news
from consultant_plus.url_parser import parse_consultant_plus_all
from klerk.url_parser import parse_klerk_all
from tinkoff.url_parser import parse_tinkoff_all
from tqdm import tqdm


__PARSERS__ = {
    "consultant_plus": parse_consultant_plus_all,
    "klerk": parse_klerk_all,
    "tinkoff": parse_tinkoff_all
}


def parse_all_sources():
    sources = json.load(open("news_parsing/sources.json"))
    result = []
    for source in sources["sources"]:
        if source["name"] in __PARSERS__:
            print(f"Start parsing {source['name'].upper()}")
            urls = __PARSERS__[source["name"]](source["base_url"])
            for url in tqdm(urls):
                result.append(parse_news(source["name"], url))
    return result


with open("parsed_news.json", "w") as file:
    json.dump(parse_all_sources(), file, ensure_ascii=False)
