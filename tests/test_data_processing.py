"""
Unit tests for data processing functions.

Run with: pytest tests/
"""

import pytest
import pandas as pd
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_processing.data_loader import clean_data, get_data_summary


class TestDataCleaning:
    """Test suite for data cleaning functions."""
    
    def test_clean_data_removes_duplicates(self):
        """Test that clean_data removes duplicate rows."""
        # Create sample data with duplicates
        data = pd.DataFrame({
            'id': [1, 2, 2, 3],
            'value': [10, 20, 20, 30]
        })
        
        cleaned = clean_data(data)
        
        assert len(cleaned) == 3
        assert not cleaned.duplicated().any()
    
    def test_clean_data_with_none(self):
        """Test that clean_data handles None input."""
        result = clean_data(None)
        assert result is None
    
    def test_get_data_summary_returns_dict(self):
        """Test that get_data_summary returns a dictionary."""
        data = pd.DataFrame({
            'a': [1, 2, 3],
            'b': [4, 5, 6]
        })
        
        summary = get_data_summary(data)
        
        assert isinstance(summary, dict)
        assert 'shape' in summary
        assert 'columns' in summary
        assert summary['shape'] == (3, 2)
    
    def test_get_data_summary_with_none(self):
        """Test that get_data_summary handles None input."""
        result = get_data_summary(None)
        assert result is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
