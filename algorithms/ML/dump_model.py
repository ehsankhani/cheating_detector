import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib


# Set up directories
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

csv_file_path = os.path.join(grandparent_dir, 'DataSet', 'cheating_features_dataset.csv')
# Load the new dataset
data = pd.read_csv(csv_file_path)

# Features and Labels
X = data[
    [
        'AST Similarity',
        'Token Similarity',
        'Levenshtein Similarity',
        'Length File 1',
        'Length File 2',
        'Function Count File 1',
        'Function Count File 2',
        'Variable Count File 1',
        'Variable Count File 2',
        'Comment Ratio File 1',
        'Comment Ratio File 2',
        'Cyclomatic Complexity File 1',
        'Cyclomatic Complexity File 2'
    ]
]
y = data['Label']

# Split and preprocess
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'cheating_detector_model.pkl')

# After defining your features and labels
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scale your features

# Save the scaler for later use
joblib.dump(scaler, 'scaler.pkl')
