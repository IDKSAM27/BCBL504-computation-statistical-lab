import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

np.random.seed(42)
data_range = pd.date_range(start="2022-01-01", end="2023-01-01", freq="D")
data = pd.DataFrame({
    "Date": data_range,
    "Value_A": np.random.normal(100, 10, len(data_range)), 
    "Value_B": np.random.normal(200, 20, len(data_range))
})

data.set_index("Date", inplace=True)

def groupby_mechanist(data):
    print("\n=== GroupBy Mechanics ===")
    grouped = data.resample('M').mean()
    print(grouped)
    return grouped

def data_formats(data):
    print("\n=== Data Formats ===")
    print("\nVector Format:")
    print(data["Value_A"].head())

    print("\nMultivariete Time Series:")
    print(data.head())

def time_series_forecasting(data):
    print("\n=== Forecasting ===")
    ts = data["Value_A"]

    train = ts[:int(0.8 * len(ts))]
    test = ts[int(0.8 * len(ts)):]

    model = ExponentialSmoothing(train, seasonal = "add", seasonal_periods=30).fit()
    
    forecast = model.forecast(len(test))

    plt.figure(figsize=(12, 6))
    plt.plot(train, label="Train")
    plt.plot(forecast, label="Forecast")
    plt.legend()
    plt.title("Time series Forecasting")
    plt.show()

if __name__ == "__main__":
    print("=== Time Series Data ===")
    print(data.head())

    monthly_data = groupby_mechanist(data)

    data_formats(data)

    time_series_forecasting(data)
