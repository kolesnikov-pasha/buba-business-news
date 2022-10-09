import pickle
import os


def get_model(user_type, user_id):
    models_paths = os.listdir("data")
    model_filename = f'data/{user_id}' if user_id in models_paths else f'data/{user_type}'
    return pickle.load(model_filename)


def save_user_mode(user_id, model):
    with open(f'data/{user_id}', 'wb') as fid:
        pickle.dump(model, fid)
