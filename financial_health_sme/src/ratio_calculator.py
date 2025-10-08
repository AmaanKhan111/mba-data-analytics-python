# Computes key financial ratios.
import pandas as pd
import numpy as np

def calculate_ratios(df):
    ratios = {}
    try:
        ratios['Current Ratio'] = df['Current Assets'].sum() / df['Current Liabilities'].sum()
        ratios['Debt-to-Equity'] = df['Total Debt'].sum() / df['Shareholders Equity'].sum()
        ratios['Net Profit Margin'] = df['Net Profit'].sum() / df['Revenue'].sum()
        ratios['Return on Assets'] = df['Net Profit'].sum() / df['Total Assets'].sum()
        ratios['Operating Margin'] = df['Operating Income'].sum() / df['Revenue'].sum()
        return ratios
    except Exception as e:
        return {"error": str(e)}
