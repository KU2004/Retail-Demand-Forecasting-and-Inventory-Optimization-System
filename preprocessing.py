import pandas as pd

def preprocess(df):
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(['product','venue','date'], inplace=True)
    return df