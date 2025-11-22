import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def calculate_mean(data):
    # Calculate the mean of the data
    mean = np.mean(data)
    return mean


def calculate_median(data):
    # Calculate the median of the data
    median = np.median(data)
    return median


def calculate_mode(data):
    # Calculate the mode of the data
    mode = stats.mode(data)
    return mode


def calculate_variance(data):
    # Calculate the variance of the data
    variance = np.var(data)
    return variance


def calculate_std_dev(data):
    # Calculate the standard deviation of the data
    std_dev = np.std(data)
    return std_dev


def plot_histogram(data):
    # Plot a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="blue", alpha=0.7)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram")
    return fig
