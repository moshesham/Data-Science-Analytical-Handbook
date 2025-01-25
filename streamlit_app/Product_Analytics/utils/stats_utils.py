import numpy as np
from scipy import stats
from typing import List, Dict

def calculate_descriptive_stats(data: List[float]) -> Dict:
    """Calculates descriptive statistics for a given dataset."""
    data = np.array(data)
    unique_values = np.unique(data)
    mode_val =  stats.mode(data, keepdims=True)[0][0] if len(unique_values) < 500 else "Not well-defined"
    return {
        "Mean": np.mean(data),
        "Median": np.median(data),
        "Mode": mode_val,
        "Range": np.max(data) - np.min(data),
        "Variance": np.var(data),
        "Standard Deviation": np.std(data),
        "IQR": stats.iqr(data),
        "Skewness": stats.skew(data),
        "Kurtosis": stats.kurtosis(data),
        "25th Percentile (Q1)": np.percentile(data, 25),
        "50th Percentile (Median)": np.percentile(data, 50),
        "75th Percentile (Q3)": np.percentile(data, 75),
        "90th Percentile": np.percentile(data, 90),
    }