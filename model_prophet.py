from prophet import Prophet
import pandas as pd

def train_prophet_models(df):
    """
    Train a separate Prophet model for each (product, venue)
    """
    models = {}

    grouped = df.groupby(['product', 'venue'])

    for (product, venue), group in grouped:
        temp = group[['date', 'sales']].rename(columns={
            'date': 'ds',
            'sales': 'y'
        })

        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )

        model.fit(temp)

        models[(product, venue)] = model

    return models


def forecast_prophet(models, df, periods=30):
    """
    Generate future forecasts for each (product, venue)
    """
    results = []

    for (product, venue), model in models.items():
        future = model.make_future_dataframe(periods=periods)

        forecast = model.predict(future)

        forecast['product'] = product
        forecast['venue'] = venue

        # Keep only useful columns
        forecast = forecast[['ds', 'yhat', 'product', 'venue']]

        results.append(forecast)

    final_forecast = pd.concat(results)

    final_forecast.rename(columns={
        'ds': 'date',
        'yhat': 'forecast'
    }, inplace=True)

    return final_forecast