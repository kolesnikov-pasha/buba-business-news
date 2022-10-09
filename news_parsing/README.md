# News parsing system

### How to build and run

```
docker build -t news-parser .
docker run -e GOOGLE_APPLICATION_CREDENTIALS="./.config/gcloud/application_default_credentials.json" \
      -it --rm --name news-parser-running news-parser
```
