import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Generate a synthetic dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'BloodPressure': [120, 130, 125, 140, 135, 130, 145, 150],
    'Cholesterol': ['Normal', 'High', 'Normal', 'High', 'Normal', 'High', 'Normal', 'High'],
    'Outcome': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad']
}

df = pd.DataFrame(data)

# Map categorical variables to numeric values
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Cholesterol'] = df['Cholesterol'].map({'Normal': 1, 'High': 0})
df['Outcome'] = df['Outcome'].map({'Good': 1, 'Bad': 0})

# Split the data into features (X) and target (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the KNN model
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

conf_matrix = confusion_matrix(y_test, y_pred)

# Display the results
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print("Confusion Matrix:")
print(conf_matrix)
