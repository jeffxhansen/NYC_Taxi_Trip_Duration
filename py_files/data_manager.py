import pandas as pd
from config import data_path

def get_data(verbose=False):
    
    # load the csvs
    activity_environment_df = pd.read_csv(f"{data_path}/activity_environment_data.csv")  
    personal_health_df = pd.read_csv(f"{data_path}/personal_health_data.csv")
    digital_interaction_df = pd.read_csv(f"{data_path}/digital_interaction_data.csv")
    if verbose: print('Successfully loaded in the data.')

    # merge the dataframes
    merge_df = pd.merge(activity_environment_df, personal_health_df, on="User_ID", validate="one_to_one")
    merged_df = pd.merge(merge_df, digital_interaction_df, on="User_ID", validate="one_to_one")
    if verbose: print('Finished merging.')
    
    return merged_df


def get_cleaned_data(verbose=False):
    
    # load in the joined csvs
    df = get_data(verbose)
    
    # clean the dataframe
    # Drop duplicate Timestamp columns
    df_cleaned = df.drop(columns=['Timestamp_x', 'Timestamp_y'])
    
    # return the cleaned dataframe
    return df_cleaned