# test_main.py
import unittest
from main import load_data
import pandas as pd


def test_load_data():
    # Path to the CSV file
    file_path = "./assets/datasets/credit/train.csv"

    # Load the data
    df = load_data(file_path)

    # Check that a DataFrame is returned
    assert isinstance(df, pd.DataFrame)

    # Check that the DataFrame is not empty
    assert not df.empty

    assert df.shape == (100000, 28)
