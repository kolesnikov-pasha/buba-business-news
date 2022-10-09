from surprise.prediction_algorithms import SVD
from surprise import Reader, Dataset
from surprise.model_selection import train_test_split
import pickle

with open('svd_model', 'rb') as f:
    svd = pickle.load(f)
class RecSys:
    model = svd

    @staticmethod
    def train(df):
        reader = Reader(rating_scale = (0, 1))
        dfs = Dataset.load_from_df(df, reader)
        svd_subset = 0.95
        train, _ = train_test_split(dfs, train_size = svd_subset, test_size = 1 - svd_subset)
        RecSys.model.fit(train)
    
    @staticmethod
    def score(user_id, text_id):
        prediction = RecSys.model.predict(user_id, text_id).est
        return float(prediction)