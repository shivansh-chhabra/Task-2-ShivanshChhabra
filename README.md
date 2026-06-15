# Task 2 - Data Classification Using AI

## Overview

This project demonstrates the fundamentals of supervised machine learning using the Iris dataset. The objective is to build a classification model capable of predicting the species of a flower based on its physical measurements.

The project follows a complete machine learning workflow:

1. Loading the dataset
2. Data preprocessing
3. Train-test splitting
4. Feature scaling
5. Model training using K-Nearest Neighbors (KNN)
6. Model evaluation using Accuracy, Confusion Matrix, and F1 Score

---

## Dataset

The project uses the Iris dataset provided by Scikit-learn.

Features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Target Classes:

* Setosa
* Versicolor
* Virginica

---

## Technologies Used

* Python
* Scikit-learn
* NumPy
* Pandas

---

## Machine Learning Concepts Covered

* Supervised Learning
* Classification
* Feature Scaling
* Train-Test Split
* K-Nearest Neighbors (KNN)
* Model Evaluation
* Confusion Matrix
* F1 Score

---

## Project Structure

Task-2-ShivanshChhabra/

├── main.py

├── requirements.txt

└── README.md

---

## Installation

Clone the repository: https://github.com/shivansh-chhabra/Task-2-ShivanshChhabra

git clone <repository-url>

Navigate to the project folder:

cd Task-2-ShivanshChhabra

Install dependencies:

pip install -r requirements.txt

---

## Running the Project

Execute:

python main.py

---

## Model Workflow

1. Load the Iris dataset.
2. Separate features and target labels.
3. Split the dataset into training and testing sets.
4. Standardize features using StandardScaler.
5. Train a K-Nearest Neighbors classifier.
6. Generate predictions on the test set.
7. Evaluate model performance.

---

## Results

Accuracy:

1.0

Confusion Matrix:

[[10 0 0]

[0 9 0]

[0 0 11]]

F1 Score:

1.0

The model correctly classified all test samples and achieved perfect performance on the test set.

---

## Author

Shivansh Chhabra
DecodeLabs Internship - Project 2

