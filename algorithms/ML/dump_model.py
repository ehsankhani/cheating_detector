# import pandas as pd
# import os
# import warnings
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.preprocessing import StandardScaler
# from xgboost import XGBClassifier
# from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
# from sklearn.pipeline import Pipeline
# import joblib
#
# # Suppress warnings from XGBoost
# warnings.filterwarnings(action='ignore', category=UserWarning, module='xgboost')
#
# # Set up directories
# current_dir = os.getcwd()
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
#
# csv_file_path = os.path.join(grandparent_dir, 'DataSet', 'cheating_features_dataset.csv')
#
# # Load the dataset
# data = pd.read_csv(csv_file_path)
#
# # Check for NaN values
# if data.isnull().values.any():
#     print("Warning: The dataset contains NaN values. Please handle them before proceeding.")
#
# # Features and Labels
# X = data[
#     [
#         'AST Similarity',
#         'Token Similarity',
#         'Levenshtein Similarity',
#         'Length File 1',
#         'Length File 2',
#         'Function Count File 1',
#         'Function Count File 2',
#         'Variable Count File 1',
#         'Variable Count File 2',
#         'Comment Ratio File 1',
#         'Comment Ratio File 2',
#         'Cyclomatic Complexity File 1',
#         'Cyclomatic Complexity File 2'
#     ]
# ]
# y = data['Label']
#
# # Ensure the classes are balanced
# print("Class distribution:\n", y.value_counts())
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#
# # Create a pipeline that includes scaling and model training
# pipeline = Pipeline([
#     ('scaler', StandardScaler()),
#     ('classifier', XGBClassifier(eval_metric='logloss', use_label_encoder=False, verbosity=0, random_state=42))
# ])
#
# # Hyperparameter grid for XGBoost
# param_grid = {
#     'classifier__n_estimators': [100, 200, 300],
#     'classifier__max_depth': [6, 10, 15],
#     'classifier__learning_rate': [0.01, 0.1, 0.2],
#     'classifier__subsample': [0.7, 0.8, 1.0],
#     'classifier__colsample_bytree': [0.7, 0.8, 1.0]
# }
#
# # Initialize Grid Search with cross-validation
# grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=2)
#
# # Train the model with Grid Search
# grid_search.fit(X_train, y_train)
#
# # Best model after Grid Search
# best_model = grid_search.best_estimator_
#
# # Evaluate the best model on the test set
# y_pred = best_model.predict(X_test)
# print("Best Model Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
#
# # Save the best model
# joblib.dump(best_model, 'cheating_detector_model.pkl')
#
# # Save the scaler used in the pipeline
# scaler = best_model.named_steps['scaler']
# joblib.dump(scaler, 'scaler.pkl')

#############################################################################################################
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from xgboost import XGBClassifier
import pickle
import os
from sklearn.metrics import classification_report, confusion_matrix

# Set up directories
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

csv_file_path = os.path.join(grandparent_dir, 'DataSet', 'cheating_features_dataset.csv')
data = pd.read_csv(csv_file_path)

# Split the dataset into features (X) and labels (y)
X = data.drop(columns=['Label'])
y = data['Label']

# Check class distribution
print(y.value_counts())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler on the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data using the same scaler
X_test_scaled = scaler.transform(X_test)

# Initialize the XGBoost model with class weight
model = XGBClassifier(eval_metric='logloss', scale_pos_weight=(y.value_counts()[0] / y.value_counts()[1]))

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 6, 9],
    'min_child_weight': [1, 5, 10],
    'subsample': [0.8, 0.9, 1.0],
    'colsample_bytree': [0.8, 0.9, 1.0]
}

# Setup Stratified K-Folds
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Setup GridSearchCV with Stratified K-Folds
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=skf, scoring='f1')

# Fit GridSearchCV
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters and model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

# Make predictions on the test set
y_pred = best_model.predict(X_test_scaled)

# Print the confusion matrix
print(confusion_matrix(y_test, y_pred))

# Print a classification report
print(classification_report(y_test, y_pred))

# Save the best model and scaler
with open('cheating_detector_model.pkl', 'wb') as model_file:
    pickle.dump(best_model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Best model and scaler saved.")
