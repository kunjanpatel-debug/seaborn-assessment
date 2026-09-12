"""
AI Corrected & Refactored Code (Production Quality)
Fixes:
1. Replaces .values modification with safe `.to_numpy(copy=True)` buffer.
2. Uses headless non-blocking chart export (`plt.savefig(dpi=150)` + `plt.close()`).
3. Handles median imputation for numeric anomalies cleanly.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Missing value handling
df.loc[np.random.choice(n_rows, 10, replace=False), 'order_value'] = np.nan
df.loc[np.random.choice(n_rows, 10, replace=False), 'delivery_time_mins'] = np.nan
df.loc[np.random.choice(n_rows, 8, replace=False), 'rating'] = np.nan

numeric_cols = ['order_value', 'distance_km', 'delivery_time_mins', 'rating', 'discount_pct']
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# SAFE FIX 1: Non-blocking export at >= 150 DPI
def distribution_analysis_safe():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].hist(df['order_value'], bins=15, color='#2b5c8f', edgecolor='black')
    axes[0].set_title("Order Value Distribution")
    axes[1].hist(df['delivery_time_mins'], bins=15, color='#d95f02', edgecolor='black')
    axes[1].set_title("Delivery Time Distribution")
    plt.tight_layout()
    plt.savefig('distribution_analysis_safe.png', dpi=150)
    plt.close()
    print("Exported distribution_analysis_safe.png at 150 DPI without blocking.")

# SAFE FIX 2: Explicit writable memory buffer via .to_numpy(copy=True)
def get_strongest_correlation_safe():
    corr_abs_vals = df[numeric_cols].corr(method='pearson').abs().to_numpy(copy=True)
    np.fill_diagonal(corr_abs_vals, 0)
    corr_abs_df = pd.DataFrame(corr_abs_vals, index=numeric_cols, columns=numeric_cols)
    col1, col2 = corr_abs_df.unstack().idxmax()
    max_corr = corr_abs_df.unstack().max()
    return col1, col2, max_corr

if __name__ == "__main__":
    print("Testing corrected code...")
    distribution_analysis_safe()
    col1, col2, val = get_strongest_correlation_safe()
    print(f"Max correlation: {col1} <-> {col2}: {val:.4f}")
