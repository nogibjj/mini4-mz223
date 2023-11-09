# main.py
import pandas as pd


def load_data(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe


if __name__ == "__main__":
    df = load_data("./assets/datasets/credit/train.csv")
    print(df.shape)
