
#################
# DATA CLEANING
#################

cols_to_drop = ['id', 'store_and_fwd_flag', 'dropoff_datetime']
SET_VENDOR_ID_TO_01 = True

#######################
# FEATURES PARAMETERS
#######################


features_toggle = {
    'distance': True,
    'weather': True
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