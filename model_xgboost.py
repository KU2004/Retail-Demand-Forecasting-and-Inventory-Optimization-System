from xgboost import XGBRegressor

def train_xgb(df):
    X = df[['day_of_week','month','lag_1','rolling_mean']]
    y = df['sales']
    
    model = XGBRegressor(n_estimators=100)
    model.fit(X, y)
    
    return model

def predict_xgb(model, df):
    X = df[['day_of_week','month','lag_1','rolling_mean']]
    df['forecast'] = model.predict(X)
    return df