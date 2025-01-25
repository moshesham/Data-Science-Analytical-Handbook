import numpy as np

def generate_normal_data(sample_size: int, loc: float = 15, scale: float = 5) -> np.ndarray:
    """Generates normally distributed data."""
    np.random.seed(42)
    normal_data = np.random.normal(loc=loc, scale=scale, size=sample_size)
    return np.clip(normal_data, 0, None)


def generate_right_skewed_data(sample_size: int, scale: float = 5) -> np.ndarray:
     """Generates right-skewed data."""
     np.random.seed(42)
     right_skewed_data = np.random.exponential(scale=scale, size=sample_size)
     return np.clip(right_skewed_data, 0, None)

def generate_left_skewed_data(sample_size: int, scale: float = 5, max_val: float = 20 ) -> np.ndarray:
    """Generates left-skewed data."""
    np.random.seed(42)
    left_skewed_data = max_val - np.random.exponential(scale=scale, size=sample_size)
    return np.clip(left_skewed_data, 0, max_val)