import json
from consultant_plus.url_parser import parse_consultant_plus_all


__PARSERS__ = {
    "consultant_plus": parse_consultant_plus_all
}


def parse_all_sources():
    sources = json.load(open("news_parsing/sources.json"))
    for source in sources["sources"]:
        if source["name"] in __PARSERS__:
            print(__PARSERS__[source["name"]](source["base_url"]))


parse_all_sources()
