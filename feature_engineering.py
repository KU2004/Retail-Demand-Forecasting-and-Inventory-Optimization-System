def create_features(df):
    df['day_of_week'] = df['date'].dt.weekday
    df['month'] = df['date'].dt.month

    # FIX: use transform instead of rolling().reset_index()
    df['lag_1'] = df.groupby(['product','venue'])['sales'].transform(lambda x: x.shift(1))

    df['rolling_mean'] = df.groupby(['product','venue'])['sales'].transform(
        lambda x: x.rolling(7).mean()
    )

    df.fillna(0, inplace=True)

    return df