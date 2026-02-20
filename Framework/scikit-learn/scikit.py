from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd

# 1. Load a standard dataset provided by scikit-learn
# The Iris dataset is a classic for classification
iris = load_iris()
X = iris.data
y = iris.target

# Optional: You can inspect the feature and target names
# print("Feature names:", iris.feature_names)
# print("Target names:", iris.target_names)

# 2. Split data into training and testing sets
# This is crucial for evaluating how well the model generalizes to new data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Choose a model and set hyperparameters
# We'll use a Random Forest Classifier, an ensemble method
model = RandomForestClassifier(random_state=42)

# 4. Train the model (fit)
# The model learns patterns from the training data
model.fit(X_train, y_train)

# 5. Make predictions
# Use the trained model to predict outcomes on the test data
predictions = model.predict(X_test)

# 6. Evaluate the model's performance
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2f}")

# Example of a single prediction
# Let's predict the class for the first test sample
first_test_sample = X_test[0].reshape(1, -1) # Reshape to 2D array for a single sample
predicted_class_index = model.predict(first_test_sample)
predicted_class_name = iris.target_names[predicted_class_index[0]]

print(f"\nPrediction for the first test sample: {predicted_class_name}")
print(f"Actual class for the first test sample: {iris.target_names[y_test[0]]}")
