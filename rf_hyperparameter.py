import pandas as pd
import numpy as np
from py_files.data_manager import get_train_data, get_test_data, get_X_y
from py_files.helper_funcs import set_np_pd_display_params
from py_files.features import generate_features
import numpy as np
import pandas as pd
from copy import deepcopy
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

set_np_pd_display_params(np, pd)


X, y = get_X_y(force_clean=True)
feature_X = generate_features(X, y)

feature_X = feature_X.drop(columns=['pickup_datetime'])

X_train = feature_X.copy()
y_train = y.copy()
X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

sample_per_class = 4
df = X_train.copy()
df = df.sort_values(by='avg_cluster_duration')

dfs = []

for _ in range(sample_per_class):
    firsts = df['avg_cluster_duration'] != df['avg_cluster_duration'].shift(1)
    dfs.append(df.loc[firsts].copy())
    df = df.loc[~firsts].copy()

final_df = pd.concat(dfs, axis=0).sort_values('avg_cluster_duration')
X_train = final_df.copy().sample(frac=1)
y_train = y_train.loc[X_train.index]

X_train = X_train.values.astype(np.float32)
y_train = y_train.values.astype(np.float32)

print(X_train.shape)
print(y_train.shape)

# Create a GridSearchCV object and get the optimal parameters and best score
param_grid = {
    'n_estimators': [100, 200, 400, 800, 1000],
    'max_depth': [None, 3, 5, 10, 20],
    'max_features': ['sqrt', 'log2'],
    'min_samples_leaf': [1, 2, 3, 5],
}


fits = np.product([len(param) for param in param_grid.values()]) * 4\

rf = RandomForestRegressor(warm_start=False)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, verbose=3, n_jobs=-2, cv=4, scoring='neg_root_mean_squared_error').fit(X_train, y_train)

with open("models/rf_grid_search.pkl", "wb") as f:
    pickle.dump(grid_search, f)