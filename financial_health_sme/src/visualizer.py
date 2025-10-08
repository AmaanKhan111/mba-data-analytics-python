# Plots ratio comparisons.

import matplotlib.pyplot as plt

def plot_ratios(ratios):
    keys = list(ratios.keys())
    values = list(ratios.values())
    plt.barh(keys, values)
    plt.xlabel('Value')
    plt.title('Financial Ratios')
    return plt