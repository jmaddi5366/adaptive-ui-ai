import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Sample data: Imagine these are user interactions with an app or website
data = {
    'user_id': [1, 2, 3, 4, 5],
    'interaction_score': [5, 3, 4, 2, 5],  # Scores represent user preferences
    'feature_1': [10, 20, 30, 40, 50],     # Example feature (e.g., time spent on page)
    'feature_2': [100, 200, 300, 400, 500] # Example feature (e.g., frequency of visits)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Prepare input features and target label
X = df[['feature_1', 'feature_2']]  # Features
y = df['interaction_score']  # Target: User preference score

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple neural network model to predict user preference
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output: predicted preference score
])

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
model.fit(X_train, y_train, epochs=50, batch_size=1)

# Predict user preferences on new data
predicted_preferences = model.predict(X_test)

# Print the predicted preferences for testing
print("Predicted User Preferences: ", predicted_preferences)
