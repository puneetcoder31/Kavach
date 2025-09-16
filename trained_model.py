# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load dataset
data = pd.read_csv("packets.csv")

# Encode categorical columns
le_protocol = LabelEncoder()
le_flag = LabelEncoder()

data['protocol'] = le_protocol.fit_transform(data['protocol'])
data['flag'] = le_flag.fit_transform(data['flag'])

# Features and Labels
X = data[['src_port', 'dst_port', 'protocol', 'flag', 'raw']]
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model + encoders
os.makedirs("backend", exist_ok=True)
joblib.dump({
    "model": model,
    "le_protocol": le_protocol,
    "le_flag": le_flag
}, "backend/model.pkl")

print("✅ Model trained with dataset & saved at backend/model.pkl")
