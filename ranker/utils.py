from google.cloud import storage
import json
import torch
from transformers import AutoTokenizer, AutoModel
from model_repository import get_model


class Embedder:
    tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
    model = AutoModel.from_pretrained("cointegrated/rubert-tiny")

    @staticmethod
    def embed_bert_cls(text):
        t = Embedder.tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = Embedder.model(
                **{k: v.to(Embedder.model.device) for k, v in t.items()}
            )
        embeddings = model_output.last_hidden_state[:, 0, :]
        embeddings = torch.nn.functional.normalize(embeddings)
        res = list(embeddings[0].cpu().numpy())

        return res

    @staticmethod
    def embed_news(news_model):

        embedded_title = Embedder.embed_bert_cls(news_model["title"])
        embedded_maintext = Embedder.embed_bert_cls(news_model["maintext"])

        return embedded_title + embedded_maintext


__cache__ = {}


def __get_news_embed__(news_id):
    if news_id in __cache__:
        return __cache__[news_id]
    storage_client = storage.Client()
    bucket = storage_client.bucket("buba_news_data")
    news = json.loads(bucket.blob(news_id).download_as_string())
    embed = Embedder.embed_news(news)
    __cache__[news_id] = embed
    return embed
