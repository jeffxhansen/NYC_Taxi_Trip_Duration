import pandas as pd
from config import data_path

def get_data():

    
    # load the csvs
    activity_environment_df = pd.read_csv(f"{data_path}/data/activity_environment_data.csv")  
    personal_health_df = pd.read_csv(f"{data_path}/data/personal_health_data.csv")
    digital_interaction_df = pd.read_csv(f"{data_path}/data/digital_interaction_data.csv")
    print('Successfully loaded in the data.')
    
    return activity_environment_df, personal_health_df, digital_interaction_df
    
    # merge the dataframes
    merge_df = pd.merge(activity_environment_df, personal_health_df, on="User_ID", validate="one_to_one")
    merged_df = pd.merge(merge_df, digital_interaction_df, on="User_ID", validate="one_to_one")
    print('Finished merging.')
    
    return merged_df


def get_cleaned_data():
    
    # load in the joined csvs
    df = get_data()
    
    # clean the dataframe
    df_cleaned = df
    
    # return the cleaned dataframe
    return df_cleaned