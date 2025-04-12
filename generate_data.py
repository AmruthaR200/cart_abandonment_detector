import pandas as pd
import numpy as np

# Generate dummy data
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'time_on_site': np.random.uniform(1, 30, n),  # minutes
    'pages_viewed': np.random.randint(1, 20, n),
    'cart_value': np.random.uniform(5, 500, n),
})

# Define abandonment condition
data['abandoned'] = ((data['time_on_site'] < 5) & (data['cart_value'] > 100) & (data['pages_viewed'] < 5)).astype(int)

# Save to CSV
data.to_csv("cart_data.csv", index=False)
print("✅ Dataset saved as cart_data.csv")
