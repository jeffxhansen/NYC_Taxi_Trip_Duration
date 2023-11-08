# NYC_Taxi_Trip_Duration Predictor

# Dataset link

https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview

Weather:
https://www.kaggle.com/datasets/aadimator/nyc-weather-2016-to-2022

## Research Question (Markdown)
1. Why your question is interesting, well thought out, precisely formulated, and answerable with the data and machine learning
2. Briefly review what is already known about your research questions and what techniques others have used to study these questions. (references to prior work)
3. Explain the data set, before analysis.
4. Form a thoughtful hypothesis or hypotheses about the data. Answer the following questions and any others that may be relevant to your question and your data set:
Where did the data come from?
Why is the data set legitimate? What weaknesses or problems does the data set have?
Why is this a good choice of data set to answer your research questions?
What do you expect your analysis to reveal?
What other interesting questions will analyzing this data answer?

## Data Cleaning / Feature Engineering (Code)
1. Organize and format your data.
2. Detect and correct (or remove) problems like missing, badly formatted, or incorrect data.
3. (Markdown) Justify your choices of what you removed, edited, reformatted, or left unchanged.
4. Apply various data handling techniques to engineer additional features that may be useful for answering your research questions.

## Robustness (Code)
1. Data cleaning code should be easy to modify for similar data sets, or handle more data points.

## Data Visualization and Basic Analysis (Code): 
1. Analyze the data, draw conclusions, and effectively communicate your main observations and results.
2. Calculate appropriate summary statistics.
3. Use appropriate isualizations and other tools to thoughtfully identify and evaluate what the data is telling you andhow well suited the data are to answering your problem
4. Make it pretty! (See below.)

## Learning Algorithms and In-depth Analysis (Code): 
1. Analyze the data using the techniques discussed in class.
2. (Markdown) Explain what research questions you can answer using the techniques presented this semester.
3. (Markdown) Explain the results of your analysis, whether the results are meaningful, and why you chose the tools that you used.
4. Don't falsify results

## Ethical Implications (Markdown): 
1. Analyze the ethical implications of your research questions, the data you gathered, and the analysis that was performed.
2. Are there privacy or other implications from the collection or use of the data?
3. Could your results and methods be misused or misunderstood?
4. What can and should be done to prevent misuse and misunderstanding?
5. Could your algorithms and methods result in a destructive self-fulfilling feedback loop?
6. How could that be prevented or controlled?
7. What other ethical implications does your work have?


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
