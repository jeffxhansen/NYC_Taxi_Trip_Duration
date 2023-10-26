import xgboost as xgb

def train_model(model, X_train, y_train, params=None):
    
    if params is None:
        params = {}
    
    model.fit(X_train, y_train)
    
    return model

def test_model(model, X_test, y_test, params=None):
    
    if params is None:
        params = {}
    
    y_pred = model.predict(X_test)
    
    # other code
    
    return y_pred

def create_model(params=None):
    
    if params is None:
        model = xgb.XGBClassifier()
    else:
        model = xgb.XGBClassifier(**params)
        
    return model
    

