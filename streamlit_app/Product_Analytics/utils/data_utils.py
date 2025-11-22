# utils/data_utils.py
import numpy as np
import pandas as pd


def generate_normal_data(
    sample_size: int, loc: float = 15, scale: float = 5
) -> np.ndarray:
    """Generates normally distributed data."""
    np.random.seed(42)
    normal_data = np.random.normal(loc=loc, scale=scale, size=sample_size)
    return np.clip(normal_data, 0, None)


def generate_right_skewed_data(sample_size: int, scale: float = 5) -> np.ndarray:
    """Generates right-skewed data."""
    np.random.seed(42)
    right_skewed_data = np.random.exponential(scale=scale, size=sample_size)
    return np.clip(right_skewed_data, 0, None)


def generate_left_skewed_data(
    sample_size: int, scale: float = 5, max_val: float = 20
) -> np.ndarray:
    """Generates left-skewed data."""
    np.random.seed(42)
    left_skewed_data = max_val - np.random.exponential(scale=scale, size=sample_size)
    return np.clip(left_skewed_data, 0, max_val)


def generate_time_series_data(
    start_date: str = "2023-01-01",
    periods: int = 365,
    freq: str = "D",
    base_value: float = 100,
    trend: float = 0.1,
    seasonality_amplitude: float = 10,
    noise_scale: float = 5,
) -> pd.DataFrame:
    """Generates time series data with trend, seasonality, and noise."""
    np.random.seed(42)
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    time_index = np.arange(periods)

    trend_component = trend * time_index
    seasonal_component = seasonality_amplitude * np.sin(
        2 * np.pi * time_index / 30
    )  # Monthly seasonality
    noise_component = np.random.normal(0, noise_scale, periods)

    time_series_values = (
        base_value + trend_component + seasonal_component + noise_component
    )
    df = pd.DataFrame({"date": date_range, "value": time_series_values})

    return df
