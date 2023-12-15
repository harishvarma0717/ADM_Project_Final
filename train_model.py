# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
data = pd.read_csv('C:/Users/harish varma/Fall 2023/myproject/data/engine_data.csv')

# Separate features (X) and target variable (y)
X = data.drop("Engine_Condition", axis=1)
y = data["Engine_Condition"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
clf = RandomForestClassifier()

# Train the model
clf.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(clf, 'random_forest_model.pkl')

# Print the model accuracy on the test set
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")
