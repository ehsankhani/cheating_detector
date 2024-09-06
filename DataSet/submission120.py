from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train a Support Vector Machine model
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

# Dump the trained model using pickle
with open('svm_model.pkl', 'wb') as file:
    pickle.dump(model, file)
