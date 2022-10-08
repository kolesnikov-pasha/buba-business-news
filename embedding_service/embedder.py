import torch
from transformers import AutoTokenizer, AutoModel
from models import NewsModel


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
    def embed_news(news_model: NewsModel):

        embedded_title = Embedder.embed_bert_cls(news_model.title)
        embedded_maintext = Embedder.embed_bert_cls(news_model.maintext)

        return embedded_title + embedded_maintext
