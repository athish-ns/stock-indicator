import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from CSV
file_path = 'gail_cleaned.csv'
df = pd.read_csv(file_path)

# Check for and handle invalid values
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

# Select features (X) and target variable (y)
features = df.drop(['Close'], axis=1)  # Remove 'Close' column as it is the target variable
target = df['Close']

# Store the 'Date' column
date_column = df['Date']

# Drop the 'Signal' column
df = df.drop(['Signal'], axis=1)

# Scale the features to handle outliers
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Train the XGBoost model
model = XGBRegressor()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Generate future dates for the next 5 years
last_date = pd.to_datetime(date_column).max()
future_dates = pd.date_range(last_date, periods=365*5, freq='B')  # Assuming business days

# Create future features for prediction
future_features = pd.DataFrame(index=future_dates, columns=features.columns)

# Make predictions for the next 5 years
future_features_scaled = scaler.transform(future_features)
future_predictions = model.predict(future_features_scaled)

# Visualize predictions
plt.plot(date_column, target, label='Actual Prices')
plt.plot(future_dates, future_predictions, label='Predicted Prices', linestyle='--', color='orange')
plt.xlabel('Date')
plt.ylabel('Stock Price (Close)')
plt.title('Stock Price Prediction for the Next 5 Years')
plt.legend()
plt.show()
