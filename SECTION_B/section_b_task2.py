import pandas as pd
import numpy as np

np.random.seed(42)
restaurants = ['Spice Hub', 'Pizza Palace', 'Biryani Blues', 'Burger King', 'Chai Point']
cities = ['Mumbai', 'Delhi', 'Bangalore']
cuisines = ['Indian', 'Fast Food', 'Beverages']

df = pd.DataFrame({
    'restaurant_name': np.random.choice(restaurants, 50),
    'city': np.random.choice(cities, 50),
    'order_value': np.random.uniform(150, 800, 50).round(2),
    'delivery_time_mins': np.random.uniform(20, 45, 50).round(1),
    'rating': np.random.uniform(3.5, 5.0, 50).round(1),
    'cuisine_type': np.random.choice(cuisines, 50)
})

# Single method chain: groupby and agg
res_summary = (
    df.groupby('restaurant_name')
    .agg(
        mean_order_value=('order_value', 'mean'),
        mean_delivery_time=('delivery_time_mins', 'mean'),
        mean_rating=('rating', 'mean')
    )
)

# Filter: rating > 4.0 and delivery time < 35 mins
filtered = res_summary[
    (res_summary['mean_rating'] > 4.0) & 
    (res_summary['mean_delivery_time'] < 35.0)
]

# Sort descending by mean_order_value, reset index, and display
final_result = filtered.sort_values(by='mean_order_value', ascending=False).reset_index()

print("--- Top Performing Restaurants Summary ---")
print(final_result.to_string(index=False))
