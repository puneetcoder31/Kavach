# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example dummy dataset
data = pd.DataFrame({
    'packet_size': [60, 500, 1500, 70, 1000],
    'protocol': [6, 17, 6, 1, 17],  # 6=TCP, 17=UDP, 1=ICMP
    'label': [0, 1, 1, 0, 1]        # 0=safe, 1=malicious
})

X = data[['packet_size', 'protocol']]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "backend/model.pkl")

print("✅ Model trained & saved as model.pkl")
