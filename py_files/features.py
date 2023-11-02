from config import features_toggle
import numpy as np


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


def generate_features(df):
    
    # from the dataframe generate the features

    
    # append the features to the dataframe
    feature_df = df

    # add the distance feature
    if features_toggle['distance']:
        feature_df = distance(feature_df)
    
    # return the feature dataframe
    return feature_df