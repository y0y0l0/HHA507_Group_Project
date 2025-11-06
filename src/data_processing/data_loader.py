"""
Data Processing Module

This module contains functions for loading, cleaning, and preprocessing healthcare data.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully. Shape: {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def clean_data(df):
    """
    Clean the dataset by handling missing values and removing duplicates.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    if df is None:
        return None
    
    # Remove duplicates
    df_cleaned = df.drop_duplicates()
    
    # Report on missing values
    missing_summary = df_cleaned.isnull().sum()
    if missing_summary.sum() > 0:
        print("\nMissing values per column:")
        print(missing_summary[missing_summary > 0])
    
    return df_cleaned


def get_data_summary(df):
    """
    Generate a summary of the dataset.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        dict: Summary statistics
    """
    if df is None:
        return None
    
    summary = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df.describe().to_dict()
    }
    
    return summary


if __name__ == "__main__":
    # Example usage
    print("Data processing module loaded successfully.")
    print("Import this module in your scripts to use these functions.")
