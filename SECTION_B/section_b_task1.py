import numpy as np

# 1. Generate 1D array of 25 distances (seed=42)
np.random.seed(42)
distances = np.random.uniform(1.0, 15.0, 25)

# 2. Vectorised fee calculation
fees = 20 + 5 * distances

# 3. Boolean indexing for orders where fee > 60
qualifying = fees > 60
qual_distances = distances[qualifying]
qual_fees = fees[qualifying]

print("--- Qualifying Orders (Delivery Fee > Rs 60) ---")
for d, f in zip(qual_distances, qual_fees):
    print(f"Distance: {d:6.2f} km | Delivery Fee: Rs {f:6.2f}")

# 4. Statistical summary
print("\n--- Delivery Fee Statistics ---")
print(f"Minimum Fee        : Rs {np.min(fees):.2f}")
print(f"Maximum Fee        : Rs {np.max(fees):.2f}")
print(f"Mean Fee           : Rs {np.mean(fees):.2f}")
print(f"Standard Deviation : Rs {np.std(fees):.2f}")
