import json
from model_repository import get_model
import utils


def __get_user_type__(user_id):
    with open("ranker/data/user_data.json", "r") as f:
        return json.load(f)[user_id]["type"]


def create_user(user_type, user_id):
    with open("ranker/data/user_data.json", "rw") as f:
        users = json.load(f)
        users[user_id] = users[user_type]
        json.dump(users, f)


def get_score(user_id, news_id):
    model = get_model(__get_user_type__(user_id), user_id)
    return model(utils.__get_news_embed__(news_id))


def mark_news_view(user_id, news_id):
    with open("ranker/data/user_data.json", "rw") as f:
        users = json.load(f)
        users[user_id]["viewed"].append(news_id)
        json.dump(users, f)


def mark_news_clicked(user_id, news_id):
    with open("ranker/data/user_data.json", "rw") as f:
        users = json.load(f)
        users[user_id]["clicked"].append(news_id)
        json.dump(users, f)
