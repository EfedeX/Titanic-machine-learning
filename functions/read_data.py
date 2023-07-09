from pathlib import Path

import pandas as pd

from read_yaml import read_yaml

relative_data_path = Path('../data/raw/')
relative_yaml_path = Path('../settings.yaml')

data_variable_names = read_yaml(relative_yaml_path)
test_name = data_variable_names['testing_data_file']
train_name = data_variable_names['training_data_file']

def read_dataframes_pandas():
    test_df = pd.read_csv(relative_data_path / test_name)
    train_df = pd.read_csv(relative_data_path / train_name)
    print("First 5 rows from the training dataFrame: \n", train_df.head())
    print("First 5 rows from the testing dataFrame: \n", test_df.head())
    return train_df, test_df

read_dataframes_pandas()