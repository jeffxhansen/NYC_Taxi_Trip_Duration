import pandas as pd
from config import (
    data_path, cols_to_drop, SET_VENDOR_ID_TO_01
)
from py_files.helper_funcs import p
import os

def clean_data(df, df_name, verbose=False):
    """loads in the train.csv and test.csv and cleans them according
    to the constants in config.py. Saves the cleaned dataframes as
    train_clean.csv and test_clean.csv
    """
    # only keep the relevant columns based on the config
    p("dropping columns") if verbose else None
    curr_cols_to_drop = [c for c in df.columns if c in cols_to_drop]
    df_clean = df.drop(columns=curr_cols_to_drop)
    p() if verbose else None
    
    # setting vendor_id to a 0 or 1 instead of 1 and 2
    if SET_VENDOR_ID_TO_01:
        p("setting vendor_id to 0 or 1") if verbose else None
        df_clean['vendor_id'] = df_clean['vendor_id'] - 1
        p() if verbose else None
    
    # other cleaning
    # ...
    
    # save the cleaned dataframe
    p("saving cleaned dataframe") if verbose else None
    df_clean.to_csv(f"{data_path}/{df_name}_clean.csv", index=False)
    p() if verbose else None
    
    return df_clean
    
    
def get_train_data():
    """either creates the cleaned train dataframe from the train.csv
    or it loads it from the data folder
    """
    if not os.path.exists(f"{data_path}/train_clean.csv"):
        train = pd.read_csv(f"{data_path}/train.csv")
        return clean_data(train, 'train')
    else:
        return pd.read_csv(f"{data_path}/train_clean.csv")
    
def get_X_y(return_np=False):
    """returns the X and y dataframes from a dataframe
    """
    df = get_train_data()
    X = df.drop(columns=['trip_duration'])
    y = df['trip_duration']
    
    if return_np:
        X, y = X.values, y.values
        
    return X, y


def get_test_data():
    """either creates the cleaned test dataframe from the test.csv
    or it loads it from the data folder
    """
    if not os.path.exists(f"{data_path}/test_clean.csv"):
        test = pd.read_csv(f"{data_path}/test.csv")
        return clean_data(test, 'test')
    else:
        return pd.read_csv(f"{data_path}/test_clean.csv")
