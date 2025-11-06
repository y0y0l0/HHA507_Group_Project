"""
Visualization Module

This module contains functions for creating visualizations of healthcare data.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def setup_style():
    """Set up the plotting style."""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12


def plot_distribution(df, column, title=None):
    """
    Plot the distribution of a numeric variable.
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column name to plot
        title (str): Plot title (optional)
    """
    setup_style()
    
    if column not in df.columns:
        print(f"Error: Column '{column}' not found")
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Histogram
    ax1.hist(df[column].dropna(), bins=30, edgecolor='black', alpha=0.7)
    ax1.set_xlabel(column)
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'Distribution of {column}')
    
    # Box plot
    ax2.boxplot(df[column].dropna())
    ax2.set_ylabel(column)
    ax2.set_title(f'Box Plot of {column}')
    
    if title:
        fig.suptitle(title, fontsize=16)
    
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df, columns=None, title='Correlation Heatmap'):
    """
    Plot a correlation heatmap.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list): List of columns to include (optional)
        title (str): Plot title
    """
    setup_style()
    
    if columns is None:
        numeric_df = df.select_dtypes(include=[np.number])
    else:
        numeric_df = df[columns]
    
    correlation_matrix = numeric_df.corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', 
                cmap='coolwarm', center=0, square=True,
                linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_group_comparison(df, group_column, value_column, title=None):
    """
    Create a box plot comparing values across groups.
    
    Args:
        df (pd.DataFrame): Input dataframe
        group_column (str): Column for grouping
        value_column (str): Column with values to compare
        title (str): Plot title (optional)
    """
    setup_style()
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=group_column, y=value_column)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel(group_column)
    plt.ylabel(value_column)
    
    if title:
        plt.title(title)
    else:
        plt.title(f'{value_column} by {group_column}')
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example usage
    print("Visualization module loaded successfully.")
    print("Import this module in your scripts to use these functions.")
