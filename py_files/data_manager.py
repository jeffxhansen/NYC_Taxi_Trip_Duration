import pandas as pd

def get_data():
    
    # load the csvs
    activity_environment_df = pd.read_csv(f"{data_path}/activity_environment_data.csv")  
    personal_health_df = pd.read_csv(f"{data_path}/personal_health_data.csv")
    digital_interaction_df = pd.read_csv(f"{data_path}/digital_interaction_data.csv")
    
    # merge the dataframes
    merged_df = None
    
    return merged_df


def get_cleaned_data():
    
    # load in the joined csvs
    df = get_data()
    
    # clean the dataframe
    df_cleaned = df
    
    # return the cleaned dataframe
    return df_cleaned