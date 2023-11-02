# NYC_Taxi_Trip_Duration Predictor

# Dataset link

https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview

Weather:
https://www.kaggle.com/datasets/aadimator/nyc-weather-2016-to-2022

# project outline

* py_files/data_manager.py
    * this will be the py file with functions like:
        * get_data() - that pulls in the merged csvs
        * get_cleaned_data() - handles any data cleaning
* py_files/features.py
    * this will handle all of the features logic
        * generate_features() - takes in a cleaned dataframe and adds all of the feature columns
* py_files/ml.py
    * this will handle all of the machine learning logic
        * train()
        * test()
        * create_model()
* py_files/helper_funcs.py
    * this will contain miscelaneous function that are used for many of the py files. They generally handle general-logic things
* config.py
    * all hyperparameters and constants for all of our code
        * features_toggle - a dictionary with True/False toggles that specify which features we will use
        * TRAIN_TEST_PERCENTAGE - the size of the train test split (probably going to be 0.80)
* analysis.ipynb
    * this will be where we have all of our graphs and charts that output performance for the ml model
    * this can also have some preliminary data analytics
* wh_predictor.ipynb
    * the final ipynb that we will submit as our writeup
* jeff.ipynb
    * jeff's personal notebook where they do all of their development and analysis before adding to the py files
* dylan.ipynb
    * dylan's personal notebook where they do all of their development and analysis before adding to the py files
* jason.ipynb
    * jason's personal notebook where they do all of their development and analysis before adding to the py files
* dallin.ipynb
    * dallin's personal notebook where they do all of their development and analysis before adding to the py files



