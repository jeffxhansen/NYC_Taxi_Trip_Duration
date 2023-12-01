import pandas as pd
import os
import numpy as np
import json
import geopandas as gpd
from shapely.wkt import loads

from config import (
    data_path, cols_to_drop, SET_VENDOR_ID_TO_01,
    PICKUP_TIME_TO_NORMALIZED_FLOAT
)
from py_files.helper_funcs import p


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

    # Drop rows with trip duration < 60 seconds
    p("dropping rows with trip duration < 60 seconds") if verbose else None
    df_clean = df_clean[df_clean['trip_duration'] >= 60]

    # Drop rows with outlier locations
    p("dropping rows with outlier locations") if verbose else None
    json_file_path = './misc/lat_long_bounds.json'
    # Read in coordinates
    with open(json_file_path, 'r') as json_file:
        # Load the JSON data from the file
        coords = json.load(json_file)
    df_clean = df_clean[(df_clean['pickup_latitude'] >= coords['lat']['min']) & (
        df_clean['pickup_latitude'] <= coords['lat']['max'])]
    df_clean = df_clean[(df_clean['pickup_longitude'] >= coords['lon']['min']) & (
        df_clean['pickup_longitude'] <= coords['lon']['max'])]
    df_clean = df_clean[(df_clean['dropoff_latitude'] >= coords['lat']['min']) & (
        df_clean['dropoff_latitude'] <= coords['lat']['max'])]
    df_clean = df_clean[(df_clean['dropoff_longitude'] >= coords['lon']['min']) & (
        df_clean['dropoff_longitude'] <= coords['lon']['max'])]

    # Keep only <99.5% of trip duration
    p("dropping rows with trip duration > 99.5%") if verbose else None
    df_clean = df_clean[df_clean['trip_duration'] <=
                        df_clean['trip_duration'].quantile(0.995)]

    # Split apart pickup_datetime
    df_clean['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df_clean['pickup_month'] = df_clean['pickup_datetime'].dt.month
    df_clean['pickup_day'] = df_clean['pickup_datetime'].dt.day_name()
    df_clean = pd.get_dummies(
        df_clean, columns=['pickup_day'], drop_first=True)
    df_clean['pickup_hour'] = df_clean['pickup_datetime'].dt.hour
    df_clean['pickup_minute'] = df_clean['pickup_datetime'].dt.minute

    # Create a pickup period.
    df_clean['pickup_period'] = pd.cut(df_clean['pickup_hour'], bins=[
                                       -1, 6, 12, 18, 24], labels=['night', 'morning', 'afternoon', 'evening'])

    # Get dummies for the pickup period.
    df_clean = pd.get_dummies(
        df_clean, columns=['pickup_period'], drop_first=True)

    # Add cyclic data.
    df_clean['pickup_hour_sin'] = np.sin(
        2 * np.pi * df_clean['pickup_hour'] / 24)
    df_clean['pickup_hour_cos'] = np.cos(
        2 * np.pi * df_clean['pickup_hour'] / 24)

    # convert pickup and dropoff times to floats from 0 to 1
    if PICKUP_TIME_TO_NORMALIZED_FLOAT:
        df_clean['pickup_datetime_norm'] = pd.to_datetime(
            df_clean['pickup_datetime']).view('int64') // 10**9
        df_clean['pickup_datetime_norm'] = (df_clean['pickup_datetime_norm'] - df_clean['pickup_datetime_norm'].min()) / (
            df_clean['pickup_datetime_norm'].max() - df_clean['pickup_datetime_norm'].min())

    # save the cleaned dataframe
    p("saving cleaned dataframe") if verbose else None
    df_clean.to_csv(f"{data_path}/{df_name}_clean.csv", index=False)
    p() if verbose else None

    return df_clean


def get_train_data(force_clean=False):
    """either creates the cleaned train dataframe from the train.csv
    or it loads it from the data folder
    """
    if not os.path.exists(f"{data_path}/train_clean.csv") or force_clean:
        train = pd.read_csv(f"{data_path}/train.csv")
        return clean_data(train, 'train')
    else:
        return pd.read_csv(f"{data_path}/train_clean.csv")


def get_X_y(return_np=False, force_clean=False):
    """returns the X and y dataframes from a dataframe
    """
    df = get_train_data(force_clean=force_clean)
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


def get_clean_weather():
    """loads in the NYC_Weather_2016_2022.csv and cleans it according
    to the constants in config.py. Saves the cleaned dataframe as
    weather_clean.csv
    """
    if not os.path.exists(f"{data_path}/weather_clean1.csv"):
        weather = pd.read_csv(f"{data_path}/NYC_Weather_2016_2022.csv")
        weather = weather.dropna()
        weather['time'] = pd.to_datetime(weather['time'])
        weather = weather[weather['time'] <= '2016-07-01']
        weather = weather.drop(columns=['rain (mm)',
                                        'cloudcover_low (%)',
                                        'cloudcover_mid (%)',
                                        'cloudcover_high (%)',
                                        'windspeed_10m (km/h)',
                                        'winddirection_10m (°)'])
        weather.to_csv(f"{data_path}/weather_clean1.csv", index=False)
        return weather
    else:
        return pd.read_csv(f"{data_path}/weather_clean1.csv")


def get_google_distance():
    """loads in the train_distance_matrix.csv and cleans it according
    to the constants in config.py. Saves the cleaned dataframe as
    google_distance_clean.csv
    """
    if not os.path.exists(f"{data_path}/google_distance_clean.csv"):
        google_distance = pd.read_csv(f"{data_path}/train_distance_matrix.csv")

        columns_to_keep = ['id', 'gc_distance', 'google_distance']
        google_distance = google_distance[columns_to_keep]

        google_distance.to_csv(
            f"{data_path}/google_distance_clean.csv", index=False)
        return google_distance
    else:
        return pd.read_csv(f"{data_path}/google_distance_clean.csv")
    
    
def get_nyc_gdf():
    """loads in the NYC street centerline data and returns it as a
    geopandas dataframe
    """
    nyc_df = pd.read_csv(f"{data_path}/Centerline.csv")
    nyc_df = nyc_df.loc[:, ['the_geom']]

    # Convert the "the_geom" column to Shapely geometries
    nyc_df['the_geom_geopandas'] = nyc_df['the_geom'].apply(loads)

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(nyc_df, geometry='the_geom_geopandas')
    
    return gdf
