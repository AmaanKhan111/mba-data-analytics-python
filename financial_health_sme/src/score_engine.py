def generate_health_score(ratios):
    try:
        score = 0
        if 'error' in ratios:
            return "Invalid data"
        
        # Normalize each metric (0–100 scale)
        score += min(max((ratios['Current Ratio'] / 2) * 20, 0), 20)
        score += min(max((1 - ratios['Debt-to-Equity']) * 20, 0), 20)
        score += min(max(ratios['Net Profit Margin'] * 100, 0), 20)
        score += min(max(ratios['Return on Assets'] * 100, 0), 20)
        score += min(max(ratios['Operating Margin'] * 100, 0), 20)
        
        return round(score, 2)
    except Exception as e:
        return f"Error in scoring: {e}"
