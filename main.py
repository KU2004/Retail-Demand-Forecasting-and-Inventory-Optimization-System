import pandas as pd

from src.preprocessing import preprocess
from src.feature_engineering import create_features
from src.model_xgboost import train_xgb, predict_xgb
from src.inventory_optimization import optimize_inventory

# Load data
df = pd.read_csv("data/raw_sales.csv")

# Preprocess
df = preprocess(df)

# Feature Engineering
df = create_features(df)

# Train model
model = train_xgb(df)

# Forecast
df = predict_xgb(model, df)

# Inventory Optimization
df = optimize_inventory(df)

# Save output
df.to_csv("outputs/forecast.csv", index=False)

print("Project executed successfully 🚀")