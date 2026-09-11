"""
Section C Mini Capstone Project: Food Delivery Analytics Console - Full EDA Report
Stack: Python 3 | NumPy, Pandas, Matplotlib, Seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATASET INITIALIZATION & PREPROCESSING (AT STARTUP)

np.random.seed(42)
n_rows = 250  # Exceeds the 200-row minimum requirement

restaurants = [
    'Spice Villa', 'Tandoor Box', 'Burger Street',
    'Pasta Bowl', 'Rolls Nation', 'Biryani Blues',
    'Urban Pizza', 'Chai Point'
]

# Generate synthetic food delivery dataset
df = pd.DataFrame({
    'restaurant_name': np.random.choice(restaurants, n_rows),
    'order_value': np.random.uniform(150, 950, n_rows).round(2),
    'distance_km': np.random.uniform(1.2, 18.5, n_rows).round(2),
    'delivery_time_mins': np.random.normal(32, 7, n_rows).round(1),
    'rating': np.random.uniform(2.5, 5.0, n_rows).round(1),
    'discount_pct': np.random.uniform(0, 25, n_rows).round(1)
})

# Artificially introduce null values to test automated cleanup
df.loc[np.random.choice(n_rows, 10, replace=False), 'order_value'] = np.nan
df.loc[np.random.choice(n_rows, 10, replace=False), 'delivery_time_mins'] = np.nan
df.loc[np.random.choice(n_rows, 8, replace=False), 'rating'] = np.nan

# Check for and fill any null values in numeric columns using column medians
numeric_cols = ['order_value', 'distance_km', 'delivery_time_mins', 'rating', 'discount_pct']
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)



# OPTION 1: SUMMARY STATISTICS (TECHNIQUE: NUMPY STATISTICAL FUNCTIONS)

def summary_statistics():
    """Calculates column-level descriptive metrics using NumPy vectorised methods."""
    print("\n" + "=" * 65)
    print("      OPTION 1: SUMMARY STATISTICS REPORT (NUMPY MODULE)")
    print("=" * 65)
    print(f"{'Metric Column':<22} | {'Min':<8} | {'Max':<8} | {'Mean':<8} | {'Std Dev':<8}")
    print("-" * 65)
    for col in numeric_cols:
        arr = df[col].to_numpy()
        c_min = np.min(arr)
        c_max = np.max(arr)
        c_mean = np.mean(arr)
        c_std = np.std(arr)
        print(f"{col:<22} | {c_min:<8.2f} | {c_max:<8.2f} | {c_mean:<8.2f} | {c_std:<8.2f}")
    print("=" * 65)


# OPTION 2: DISTRIBUTION ANALYSIS (TECHNIQUE: MATPLOTLIB SUBPLOTS)

def distribution_analysis():
    """Generates multi-panel histograms using Matplotlib and saves to PNG without plt.show()."""
    print("\n" + "=" * 65)
    print("   OPTION 2: DISTRIBUTION ANALYSIS (MATPLOTLIB SUBPLOTS)")
    print("=" * 65)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Order Value & Delivery Duration Distributions", fontsize=15, fontweight='bold')

    # Subplot 1: Order Value
    axes[0].hist(df['order_value'], bins=15, color='#2b5c8f', edgecolor='black', alpha=0.85)
    axes[0].set_title("Order Value Distribution")
    axes[0].set_xlabel("Order Value (Rs)")
    axes[0].set_ylabel("Frequency")
    axes[0].grid(axis='y', linestyle='--', alpha=0.6)

    # Subplot 2: Delivery Duration
    axes[1].hist(df['delivery_time_mins'], bins=15, color='#d95f02', edgecolor='black', alpha=0.85)
    axes[1].set_title("Delivery Time Distribution")
    axes[1].set_xlabel("Delivery Time (mins)")
    axes[1].set_ylabel("Frequency")
    axes[1].grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    output_filename = "distribution_analysis.png"
    plt.savefig(output_filename, dpi=150)
    plt.close()  # Must not display interactively
    print(f">> Successfully exported distribution chart to: {output_filename} (DPI >= 150)")


# OPTION 3: CORRELATION HEATMAP (TECHNIQUE: SEABORN VISUALISATION)

def correlation_heatmap():
    """Computes Pearson correlation and visualises using Seaborn heatmap."""
    print("\n" + "=" * 65)
    print("      OPTION 3: CORRELATION HEATMAP (SEABORN VISUALISATION)")
    print("=" * 65)
    
    plt.figure(figsize=(8, 6))
    corr_matrix = df[numeric_cols].corr(method='pearson')
    
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        fmt=".2f", 
        cmap='coolwarm', 
        vmin=-1, 
        vmax=1, 
        linewidths=0.5
    )
    plt.title("Feature Pearson Correlation Matrix", fontsize=14, pad=12)
    plt.tight_layout()
    
    output_filename = "menu_correlation_heatmap.png"
    plt.savefig(output_filename, dpi=150)
    plt.close()  # Must not display interactively
    print(f">> Successfully exported correlation heatmap to: {output_filename} (DPI >= 150)")


# OPTION 4: RESTAURANT PERFORMANCE REPORT (TECHNIQUE: PANDAS GROUPBY & AGG)

def restaurant_performance():
    """Aggregates restaurant performance metrics using Pandas groupby."""
    print("\n" + "=" * 65)
    print("   OPTION 4: RESTAURANT PERFORMANCE REPORT (PANDAS GROUPBY)")
    print("=" * 65)
    
    summary = (
        df.groupby('restaurant_name')
        .agg(
            total_orders=('order_value', 'count'),
            avg_order_value=('order_value', 'mean'),
            avg_delivery_time=('delivery_time_mins', 'mean'),
            avg_rating=('rating', 'mean')
        )
        .round(2)
        .sort_values(by='avg_rating', ascending=False)
        .reset_index()
    )
    print(summary.to_string(index=False))
    print("=" * 65)



# POST-EXIT PLAIN-TEXT SUMMARY REPORT

def display_exit_summary():
    """Generates the required plain-text analytical report after user selects Exit."""
    print("\n" + "#" * 65)
    print("             FINAL POST-ANALYSIS CONSOLE REPORT")
    print("#" * 65)
    
    # 1. Top 3 restaurants by mean rating
    top_3 = (
        df.groupby('restaurant_name')['rating']
        .mean()
        .nlargest(3)
        .round(2)
    )
    print("\n1. TOP 3 RESTAURANTS BY MEAN CUSTOMER RATING:")
    for rank, (name, score) in enumerate(top_3.items(), 1):
        print(f"   Rank {rank}: {name:<18} -> {score:.2f} / 5.0")

    # 2. Numeric column pair with highest absolute Pearson correlation
  # 2. Numeric column pair with highest absolute Pearson correlation
    corr_abs_vals = df[numeric_cols].corr(method='pearson').abs().to_numpy(copy=True)
    np.fill_diagonal(corr_abs_vals, 0)
    corr_abs_df = pd.DataFrame(corr_abs_vals, index=numeric_cols, columns=numeric_cols)
    col1, col2 = corr_abs_df.unstack().idxmax()
    max_corr_val = corr_abs_df.unstack().max()
    print("\n2. STRONGEST CORRELATED NUMERIC COLUMN PAIR:")
    print(f"   Features : {col1} <---> {col2}")
    print(f"   Strength : Absolute Pearson |r| = {max_corr_val:.4f}")

    # 3. Overall mean and standard deviation of delivery time
    overall_mean_time = np.mean(df['delivery_time_mins'])
    overall_std_time = np.std(df['delivery_time_mins'])
    print("\n3. OVERALL DELIVERY TIME DYNAMICS (FULL DATASET):")
    print(f"   Overall Mean Delivery Time : {overall_mean_time:.2f} minutes")
    print(f"   Overall Standard Deviation : {overall_std_time:.2f} minutes")
    print("#" * 65 + "\n")



# MAIN APPLICATION CONTROLLER

def main():
    while True:
        print("\n" + "=" * 50)
        print("     FOOD DELIVERY ANALYTICS CONSOLE (EDA)    ")
        print("=" * 50)
        print("1. Summary Statistics (NumPy)")
        print("2. Distribution Analysis (Matplotlib)")
        print("3. Correlation Heatmap (Seaborn)")
        print("4. Restaurant Performance Report (Pandas)")
        print("5. Exit Program")
        print("=" * 50)
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            summary_statistics()
        elif choice == '2':
            distribution_analysis()
        elif choice == '3':
            correlation_heatmap()
        elif choice == '4':
            restaurant_performance()
        elif choice == '5':
            print("\nExiting interactive console... compiling final synthesis...")
            break
        else:
            print("\n[!] Invalid input. Please enter a number from 1 to 5.")
    
    # Print the terminal summary report upon exit
    display_exit_summary()


if __name__ == "__main__":
    main()
