import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

print("📁 Current working directory:", os.getcwd())

# Step 1: Load dataset
try:
    data = pd.read_csv("cart_data.csv")
    print("✅ cart_data.csv loaded")
except FileNotFoundError:
    print("❌ cart_data.csv not found! Check the file path.")
    exit()

# Step 2: Split and train
X = data[['time_on_site', 'pages_viewed', 'cart_value']]
y = data['abandoned']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
print("✅ Model trained")

# Step 3: Save the model
model_path = os.path.join(os.getcwd(), "model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ model.pkl saved to: {model_path}")