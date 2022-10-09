import json
from model_repository import save_user_mode
import utils
from sklearn.linear_model import LogisticRegression
import numpy as np
import random
from tqdm import tqdm


def learn_model(user):
    model = LogisticRegression()
    viewed_ids = user["viewed"]
    clicked_ids = user["clicked"]
    random.shuffle(viewed_ids)
    random.shuffle(clicked_ids)
    for id in clicked_ids:
        viewed_ids.remove(id)
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for id in tqdm(viewed_ids[:100]):
        x_test.append(utils.__get_news_embed__(id))
        y_test.append(0)
    for id in tqdm(clicked_ids[:100]):
        x_test.append(utils.__get_news_embed__(id))
        y_test.append(1)
    for id in tqdm(viewed_ids[100:]):
        x_train.append(utils.__get_news_embed__(id))
        y_train.append(0)
    for id in tqdm(clicked_ids[100:]):
        x_train.append(utils.__get_news_embed__(id))
        y_train.append(1)
    print("Starting learning")
    model.fit(x_train, y_train)
    print(model.predict_proba(x_test))
    print(y_test)
    return model


with open("ranker/data/user_data.json", "r") as f:
    users = json.load(f)
    for user_id in users:
        model = learn_model(users[user_id])
        save_user_mode(user_id, model)
