from newsplease import NewsPlease
import json


"""
{
  "authors": [],
  "date_download": null,
  "date_modify": null,
  "date_publish": "2017-07-17 17:03:00",
  "description": "Russia has called on Ukraine to stick to the Minsk peace process [news-please will extract the whole text but in this example file we needed to cut off here because of copyright laws].",
  "filename": "https%3A%2F%2Fwww.rt.com%2Fnews%2F203203-ukraine-russia-troops-border%2F.json",
  "image_url": "https://img.rt.com/files/news/31/9c/30/00/canada-russia-troops-buildup-.si.jpg",
  "language": "en",
  "localpath": null,
  "source_domain": "www.rt.com",
  "maintext": "Russia has called on Ukraine to stick to the Minsk peace process [news-please will extract the whole text but in this example file we needed to cut off here because of copyright laws].",
  "title": "Moscow to Kiev: Stick to Minsk ceasefire, stop making false \u2018invasion\u2019 claims",
  "title_page": null,
  "title_rss": null,
  "url": "https://www.rt.com/news/203203-ukraine-russia-troops-border/"
}
"""
def parse_news(source_name, url):
    article = NewsPlease.from_url(url).get_dict()
    __finish_parsing__(source_name, article, url)
    article["date_publish"] = str(article["date_publish"]) if article["date_publish"] is not None else None
    article["date_download"] = str(article["date_download"]) if article["date_download"] is not None else None
    article["date_modify"] = str(article["date_modify"]) if article["date_modify"] is not None else None
    return article


def __finish_parsing__(source_name, article, url):
    # this method is making source_name-wised parsing. 
    # For example, it could extract date_publish for Consultant.Plus if it was not extracted by news-please
    pass
