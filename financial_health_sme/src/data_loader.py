# Handles uploading and reading financial data.
import pandas as pd

def load_financial_data(file):
    """Load Excel or CSV financial data."""
    try:
        df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
        return df
    except Exception as e:
        return f"Error loading file: {e}"
