import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings("ignore")

__data_columns = None
__model = None


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    with open("./artifacts/house_price_prediction.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_estimated_price(total_sqft, bath, bhk):
    # load saved artifacts
    global __data_columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    with open("./artifacts/house_price_prediction.pickle", "rb") as f:
        __model = pickle.load(f)

    # calculations
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    return round(__model.predict([x])[0], 2) * 100000 #


if __name__ == '__main__':
    load_saved_artifacts()
# print(get_estimated_price(1000, 2, 2))
# print(get_estimated_price(1000, 10, 10))
