import pandas as pd
from config import (
    data_path, cols_to_drop, nan_columns,
    dummy_cols, ordinal_mapping, binary_mapping   
)
import os

def save_merged_data():
    """loads in the csvs, merges them, and saves the merged 
    dataframe as a csv. Returns the merged dataframe
    """
    # load the csvs
    activity_environment_df = pd.read_csv(f"{data_path}/activity_environment_data.csv")  
    personal_health_df = pd.read_csv(f"{data_path}/personal_health_data.csv")
    digital_interaction_df = pd.read_csv(f"{data_path}/digital_interaction_data.csv")
    print('Successfully loaded in the data.')

    # merge all of the above dataframes on User_ID
    merged_df = activity_environment_df.merge(personal_health_df, on='User_ID')
    health_df = merged_df.merge(digital_interaction_df, on='User_ID')
    
    # save the health_df (the merged data)
    health_df.to_csv(f"{data_path}/health_data.csv")
    
    return health_df

def get_health_data():
    """either creates the merged dataframe from the separate csvs
    or it loads it from the data folder
    """
    if not os.path.exists(f"{data_path}/health_data.csv"):
        return save_merged_data()
    else:
        return pd.read_csv(f"{data_path}/health_data.csv")
    
def clean_health_df():
    """cleans the health_df and saves it as a csv. Returns the cleaned
    health_df
    """
    # load in the health_df
    health_df = get_health_data()
    
    # drop the columns that we don't need
    health_df = health_df.drop(cols_to_drop, axis=1)
    
    # fill the columns with NaNs with the string 'None'
    for col in nan_columns:
        health_df[col] = health_df[col].fillna('None')
        
    # dummy encode the categorical columns
    health_df = pd.get_dummies(health_df, columns=dummy_cols)
    new_dummy_cols = [col for col in health_df.columns if any([c in col for c in dummy_cols])]
    for col in new_dummy_cols:
        health_df[col] = health_df[col].astype(int)
        
    # map columns with an order to the categories to ints
    for col, mapping in ordinal_mapping.items():
        health_df[col] = health_df[col].map(mapping)
        
    # map binary categorical columns to ints
    for col, mapping in binary_mapping.items():
        health_df[col] = health_df[col].map(mapping).astype(int)
        
    # save the cleaned health_df
    health_df.to_csv(f"{data_path}/health_data_clean.csv")
    
    return health_df
    
    
def get_cleaned_data():
    """either creates the cleaned dataframe, saves and returns it
    or it loads it from the data folder
    """
    if not os.path.exists(f"{data_path}/health_data_clean.csv"):
        return clean_health_df()
    else:
        return pd.read_csv(f"{data_path}/health_data_clean.csv")