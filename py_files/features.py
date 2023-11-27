from config import features_toggle
from py_files.data_manager import get_clean_weather, get_google_distance
import numpy as np
import pandas as pd


def distance(df):
    """
    Calculate the Manhattan distance in kilometers between pickup and dropoff locations
    and add it as a new column 'distance_km' to the DataFrame.

    The Manhattan distance, also known as the L1 distance or taxicab distance, between two points
    on the Earth's surface is calculated by finding the absolute differences between their respective
    longitudes and latitudes and summing them up. This function computes the Manhattan distance
    in kilometers between the pickup and dropoff locations in a DataFrame, assuming a constant
    Earth radius of 6371 kilometers.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing pickup and dropoff coordinates with columns
                           'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', and 'dropoff_latitude'.

    Returns:
    pandas.DataFrame: A DataFrame with an additional 'distance_km' column representing the Manhattan
                     distance in kilometers between pickup and dropoff locations.
    """
    # Radius of the Earth in kilometers
    earth_radius_km = 6371.0

    # Get the pickup and dropoff coordinates
    lon1 = df['pickup_longitude']
    lat1 = df['pickup_latitude']
    lon2 = df['dropoff_longitude']
    lat2 = df['dropoff_latitude']

    # Convert latitude and longitude from degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])


    # Calculate the differences in latitude and longitude
    delta_lat = abs(lat1 - lat2)
    delta_lon = abs(lon1 - lon2)

    # Calculate the Manhattan distance in kilometers
    df['distance_km'] = earth_radius_km * (delta_lat + delta_lon)

    return df


def add_weather_feature(df):
    """
    Add weather-related features to a DataFrame by merging it with a weather dataset.

    This function merges the input DataFrame with a weather dataset based on the rounded pickup time
    and adds weather-related features to the DataFrame. It rounds the 'pickup_datetime' column to the
    nearest hour to match the weather data's time resolution.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing pickup-related data.

    Returns:
    pandas.DataFrame: A DataFrame with added weather-related features merged from the weather dataset.
    """
    # Get weather data
    weather = get_clean_weather()
    
    # Round the pickup time to the nearest hour (to merge with weather)
    df['rounded_date'] = pd.to_datetime(df['pickup_datetime']).dt.round('H')
    weather['time'] = pd.to_datetime(weather['time'])

    # Merge with weather
    df = df.merge(weather, left_on='rounded_date', right_on='time')

    # Drop unnecessary columns and return the dataframe
    df = df.drop(columns=['rounded_date', 'time'])
    return df


def add_google_distance(df):
    """
    Add Google Maps distance and duration features to a DataFrame by merging it with a Google Maps dataset.
    """

    # Get the google distance
    google_distance = get_google_distance()

    # Merge with the dataframe (verify 1:1)
    df = df.merge(google_distance, on='id', validate='1:1')

    return df


def generate_features(df):
    
    # from the dataframe generate the features

    
    # append the features to the dataframe
    feature_df = df

    # add the distance feature
    if features_toggle['distance']:
        feature_df = distance(feature_df)
    
    # add the weather feature
    if features_toggle['weather']:
        feature_df = add_weather_feature(feature_df)

    # add the google distance feature
    if features_toggle['google_distance']:
        feature_df = add_google_distance(feature_df)
    
    # return the feature dataframe
    return feature_df