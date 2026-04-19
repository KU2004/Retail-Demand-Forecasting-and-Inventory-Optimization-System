import pandas as pd
import numpy as np
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ==============================
# 📌 1. Save Data Function
# ==============================

def save_csv(df, path):
    """
    Save DataFrame to CSV safely
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"✅ File saved at: {path}")


# ==============================
# 📌 2. Load Data Function
# ==============================

def load_csv(path):
    """
    Load CSV with error handling
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    df = pd.read_csv(path)
    print(f"✅ Loaded data from: {path}")
    return df


# ==============================
# 📌 3. Model Evaluation Metrics
# ==============================

def evaluate_model(y_true, y_pred):
    """
    Calculate MAE and RMSE
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    print(f"📊 MAE: {mae:.2f}")
    print(f"📊 RMSE: {rmse:.2f}")
    
    return {"MAE": mae, "RMSE": rmse}


# ==============================
# 📌 4. Train-Test Split (Time Series)
# ==============================

def train_test_split_time(df, split_ratio=0.8):
    """
    Split dataset based on time (not random)
    """
    df = df.sort_values('date')
    
    split_index = int(len(df) * split_ratio)
    
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]
    
    return train, test


# ==============================
# 📌 5. Add Date Features
# ==============================

def add_date_features(df):
    """
    Add useful time-based features
    """
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.weekday
    
    return df


# ==============================
# 📌 6. Create Lag Features
# ==============================

def create_lag_features(df, lags=[1, 7]):
    """
    Create lag features for time series
    """
    for lag in lags:
        df[f'lag_{lag}'] = df.groupby(['product','venue'])['sales'].shift(lag)
    
    df.fillna(0, inplace=True)
    return df


# ==============================
# 📌 7. Create Rolling Features
# ==============================

def create_rolling_features(df, windows=[7]):
    """
    Create rolling mean features
    """
    for window in windows:
        df[f'rolling_mean_{window}'] = (
            df.groupby(['product','venue'])['sales']
            .rolling(window)
            .mean()
            .reset_index(0, drop=True)
        )
    
    df.fillna(0, inplace=True)
    return df


# ==============================
# 📌 8. Check Missing Values
# ==============================

def check_missing(df):
    """
    Display missing values summary
    """
    missing = df.isnull().sum()
    print("🔍 Missing Values:\n", missing)
    return missing


# ==============================
# 📌 9. Filter by Product & Venue
# ==============================

def filter_data(df, product=None, venue=None):
    """
    Filter dataset for dashboard or analysis
    """
    if product:
        df = df[df['product'] == product]
    if venue:
        df = df[df['venue'] == venue]
    
    return df


# ==============================
# 📌 10. Create Reorder Alerts
# ==============================

def generate_alerts(df):
    """
    Flag reorder alerts
    """
    df['reorder_alert'] = df['order_qty'].apply(
        lambda x: "⚠️ Reorder Needed" if x > 0 else "✅ Stock OK"
    )
    
    return df