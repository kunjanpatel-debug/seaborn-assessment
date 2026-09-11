import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(7)
n = 200
df = pd.DataFrame({
    'order_value': np.random.uniform(100, 800, n).round(2),
    'distance_km': np.random.uniform(1, 20, n).round(2),
    'delivery_time_mins': np.random.normal(30, 8, n).round(1),
    'rating': np.random.uniform(1.0, 5.0, n).round(1),
    'discount_pct': np.random.uniform(0, 30, n).round(1)
})

# Introduce 5% null values
df.loc[np.random.choice(n, int(0.05 * n), replace=False), 'delivery_time_mins'] = np.nan
df.loc[np.random.choice(n, int(0.05 * n), replace=False), 'rating'] = np.nan

# Fill nulls with column medians
df['delivery_time_mins'] = df['delivery_time_mins'].fillna(df['delivery_time_mins'].median())
df['rating'] = df['rating'].fillna(df['rating'].median())

# Derived speed column and 3 equal-frequency bins
df['delivery_speed_kmph'] = df['distance_km'] / (df['delivery_time_mins'] / 60)
df['speed_band'] = pd.qcut(df['delivery_speed_kmph'], q=3, labels=['Slow', 'Normal', 'Fast'])

# Heatmap of Pearson correlation
plt.figure(figsize=(8, 6))
numeric_cols = df.select_dtypes(include=[np.number])
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.close()

# Pairplot coloured by speed_band
pairplot_fig = sns.pairplot(
    df, 
    vars=['order_value', 'distance_km', 'delivery_time_mins', 'rating'], 
    hue='speed_band', 
    palette='Set1'
)
pairplot_fig.savefig('pairplot.png', dpi=150)
plt.close()

print("Generated correlation_heatmap.png and pairplot.png at 150 DPI")
