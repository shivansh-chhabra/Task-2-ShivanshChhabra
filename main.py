from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


# Load dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Train model
knn.fit(X_train, y_train)

# Predictions
predictions = knn.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
f1 = f1_score(y_test, predictions, average="weighted")

print("Accuracy:")
print(accuracy)

print("\nConfusion Matrix:")
print(cm)

print("\nF1 Score:")
print(f1)