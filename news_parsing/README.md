# News parsing system

### How to build and run

```
docker build -t news-parser .
docker run -e GOOGLE_APPLICATION_CREDENTIALS="./.config/gcloud/application_default_credentials.json" \
      -it --rm --name news-parser-running news-parser
```

### Where does collected data locate?

All posts are uploading on the Google Cloud Storage:
![imgs/gcloud_example.png]()

### News format

```
{
      "authors": ["Author 1", "Author 2"], 
      "date_download": "2022-10-08 15:29:09", 
      "date_publish": "2017-11-30 14:13:06", 
      "description": "Short desciption of news", 
      "filename": "https%3A%2F%2Fjournal.tinkoff.ru%2Fomg%2F1-mln-za-vzyatku%2F.json", 
      "image_url": "http://img-cdn.tinkoffjournal.ru/-/izum-3011.kbotse61mjxl.png", 
      "language": "ru", 
      "maintext": "News text content", 
      "source_domain": "journal.tinkoff.ru", 
      "title": "News title", 
      "url": "https://journal.tinkoff.ru/omg/1-mln-za-vzyatku/", 
      "id": "-mln-za-vzyatku", 
      "parser_version": 1
}
```