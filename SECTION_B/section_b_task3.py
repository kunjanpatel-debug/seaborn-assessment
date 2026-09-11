import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
months = [f'M{i}' for i in range(1, 13)]
orders = np.random.randint(1000, 5001, 12)
aov = np.random.uniform(200, 400, 12)
revenue = orders * aov
del_times_sim = np.random.normal(28, 4, 500)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Food Delivery Performance Dashboard', fontsize=16)

# Subplot 1 - Line chart
axes[0].plot(months, orders, marker='o', color='b', linestyle='-')
for i, txt in enumerate(orders):
    axes[0].annotate(f'{txt}', (months[i], orders[i]), textcoords="offset points", xytext=(0, 7), ha='center', fontsize=8)
axes[0].set_title('Monthly Total Orders')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Total Orders')

# Subplot 2 - Bar chart
colors = ['green' if r > 800000 else 'red' for r in revenue]
axes[1].bar(months, revenue, color=colors)
axes[1].axhline(800000, color='black', linestyle='--', label='Rs 8,00,000 Threshold')
axes[1].set_title('Monthly Revenue')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Revenue (Rs)')
axes[1].legend()

# Subplot 3 - Histogram
axes[2].hist(del_times_sim, bins=15, color='skyblue', edgecolor='black')
sample_mean = np.mean(del_times_sim)
axes[2].axvline(sample_mean, color='red', linestyle='--', label=f'Mean ({sample_mean:.1f}m)')
axes[2].set_title('Delivery Time Distribution')
axes[2].set_xlabel('Delivery Time (mins)')
axes[2].set_ylabel('Frequency')
axes[2].legend()

plt.tight_layout()
plt.savefig('food_delivery_dashboard.png', dpi=150)
print("Saved dashboard as food_delivery_dashboard.png at 150 DPI")
