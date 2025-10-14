import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Define the path to the dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'heart.csv')

# Load dataset
data = pd.read_csv(csv_path)

# Features and Target
X = data.drop(columns=['Heart Disease'])  # Adjust 'target' if your dataset uses a different name
y = data['Heart Disease']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Save the model
model_path = os.path.join(BASE_DIR, 'heart_disease_model.pkl')
joblib.dump(model, model_path)
print(f'Model saved at {model_path}')
