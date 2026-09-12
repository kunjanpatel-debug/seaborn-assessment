"""
AI Original Generated Code (Pre-Correction)
Contains:
1. Python 3.13 read-only view bug (np.fill_diagonal on .values)
2. Blocking interactive visualization calls (plt.show)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset initialization
np.random.seed(42)
n_rows = 250
restaurants = ['Spice Villa', 'Tandoor Box', 'Burger Street', 'Pasta Bowl', 'Rolls Nation', 'Biryani Blues', 'Urban Pizza', 'Chai Point']

df = pd.DataFrame({
    'restaurant_name': np.random.choice(restaurants, n_rows),
    'order_value': np.random.uniform(150, 950, n_rows).round(2),
    'distance_km': np.random.uniform(1.2, 18.5, n_rows).round(2),
    'delivery_time_mins': np.random.normal(32, 7, n_rows).round(1),
    'rating': np.random.uniform(2.5, 5.0, n_rows).round(1),
    'discount_pct': np.random.uniform(0, 25, n_rows).round(1)
})

numeric_cols = ['order_value', 'distance_km', 'delivery_time_mins', 'rating', 'discount_pct']

# BUG 1: Blocking display halts execution flow in automation pipelines
def distribution_analysis_buggy():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(df['order_value'], bins=15)
    axes[1].hist(df['delivery_time_mins'], bins=15)
    plt.show()  # HALTS EXECUTION UNTIL WINDOW IS CLOSED MANUALLY

# BUG 2: Python 3.13 / newer pandas raises ValueError: underlying array is read-only
def get_strongest_correlation_buggy():
    corr_abs = df[numeric_cols].corr(method='pearson').abs()
    np.fill_diagonal(corr_abs.values, 0)  # FAILS IN PYTHON 3.13
    col1, col2 = corr_abs.unstack().idxmax()
    max_corr = corr_abs.unstack().max()
    return col1, col2, max_corr

if __name__ == "__main__":
    print("Testing original code...")
    col1, col2, val = get_strongest_correlation_buggy()
    print(f"Max correlation: {col1} <-> {col2}: {val}")
