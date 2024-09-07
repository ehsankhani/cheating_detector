from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load the iris dataset
data = load_iris()
features = data.data
labels = data.target

# Split the dataset into training and test sets
X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(features, labels, test_size=0.25, random_state=21)

# Train a Logistic Regression classifier
classifier = LogisticRegression(max_iter=250, random_state=21)
classifier.fit(X_train_split, y_train_split)

# Save the trained model using joblib
joblib.dump(classifier, 'lr_model.pkl')
