
#################
# DATA CLEANING
#################

cols_to_drop = [
    'User_ID', 'Timestamp_x', 'Battery_Level', 
    'Timestamp_y', 'Timestamp', 'Anomaly_Flag', 
    'Screen_Time', 'Notifications_Received', 'Day_of_Week']

nan_columns = [
    'Exercise_Type', 'Exercise_Intensity', 'Medical_Conditions', 
    'Alcohol_Consumption', 'Stress_Level', 'Mood']

dummy_cols = ['Exercise_Type', 'Gender', 'Medical_Conditions', 'Mood']

ordinal_mapping = {
    'Exercise_Intensity': {
        'None': 0,
        'Low': 1,
        'Moderate': 2,
        'High': 3
    },
    'Alcohol_Consumption': {
        'None': 0,
        'Moderate': 1,
        'Heavy': 2
    },
    'Stress_Level': {
        'Low': 1,
        'Moderate': 2,
        'High': 3
    }
}

binary_mapping = {
    "ECG": {
        'Abnormal': 0,
        'Normal': 1
    }, 
    "Snoring": {
        'No': 0,
        'Yes': 1
    },
    "Smoker": {
        'No': 0,
        'Yes': 1
    },
    "Medication": {
        'No': 0,
        'Yes': 1
    }
}

#######################
# FEATURES PARAMETERS
#######################


features_toggle = {
    
}

#########
# PATHS
#########

data_path = "./data"

########################
# ML PARAMS AND TRAING
########################

TRAIN_TEST_SPLIT = 0.8

xgboost_params = {}

######################
# DISPLAY PARAMETERS
######################

NP_FLOAT_PRECISION = 7
NP_FLOAT_PRECISION_F = lambda x: "{0:0.7f}".format(x) # shows 7 decimal places
PD_FLOAT_PRECISION = 7 
PD_FLOAT_PRECISION_F = lambda x: "{0:0.7f}".format(x) # shows 7 decimal places
PD_MAX_COLUMNS = None # show all of the columns
PD_MAX_ROWS = 50 # show up to 50 rows instead of the default 20