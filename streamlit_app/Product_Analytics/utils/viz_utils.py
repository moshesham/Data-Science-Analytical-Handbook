# utils/viz_utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_histogram(data: np.ndarray, title: str = "Histogram", xlabel: str = "Value", ylabel: str = "Frequency") -> plt.Figure:
    """Plots a histogram for a given dataset."""
    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig

def plot_boxplot(data: np.ndarray, title: str = "Boxplot", ylabel: str = "Value") -> plt.Figure:
     """Plots a boxplot for a given dataset."""
     fig, ax = plt.subplots()
     sns.boxplot(y=data, ax=ax)
     ax.set_title(title)
     ax.set_ylabel(ylabel)
     return fig


def plot_distribution_comparison(data_sets: dict, title: str ="Distribution Comparison", xlabel: str = "Value", ylabel: str = "Density") -> plt.Figure:
    """Plots the distribution of multiple datasets for comparison"""
    fig, ax = plt.subplots()
    for name, data in data_sets.items():
        sns.kdeplot(data, ax=ax, label=name)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    return fig


def plot_correlation_heatmap(corr_matrix: pd.DataFrame, title: str = "Correlation Heatmap", annot: bool =True) -> plt.Figure:
    """Plots a correlation heatmap from a correlation matrix."""
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=annot, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title(title)
    return fig

def plot_scatter_with_regression(x: np.ndarray, y: np.ndarray, title: str="Scatter Plot with Regression",
                                  xlabel: str="X Variable", ylabel: str="Y Variable") -> plt.Figure:
    """Plots a scatter plot with a regression line."""
    fig, ax = plt.subplots()
    sns.regplot(x=x, y=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


def plot_multiple_histograms(data_sets: dict, title: str = "Multiple Histograms", xlabel: str = "Value", ylabel: str = "Frequency") -> plt.Figure:
    """Plots multiple histograms for given datasets in a single figure."""
    num_plots = len(data_sets)
    fig, axes = plt.subplots(1, num_plots, figsize=(15, 5))
    if num_plots == 1:
      axes = [axes]
    for i, (name, data) in enumerate(data_sets.items()):
        sns.histplot(data, kde=True, ax=axes[i], color=f'C{i}')
        axes[i].set_title(f"Histogram of {name} Data")
        axes[i].set_xlabel(xlabel)
        axes[i].set_ylabel(ylabel)
    fig.suptitle(title)
    plt.tight_layout()
    return fig


def plot_multiple_boxplots(data_sets: dict, title: str = "Multiple Boxplots", ylabel: str = "Value") -> plt.Figure:
  """Plots multiple boxplots for given datasets in a single figure."""
  num_plots = len(data_sets)
  fig, axes = plt.subplots(1, num_plots, figsize=(15, 5))

  if num_plots == 1:
    axes = [axes]
  for i, (name, data) in enumerate(data_sets.items()):
    sns.boxplot(y=data, ax=axes[i], color=f'C{i}')
    axes[i].set_title(f"Boxplot of {name} Data")
    axes[i].set_ylabel(ylabel)
  fig.suptitle(title)
  plt.tight_layout()
  return fig