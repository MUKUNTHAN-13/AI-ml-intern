Heart Disease Prediction – Decision Trees & Random Forests
1.Project Overview

This project uses the Heart Disease dataset to build and evaluate Decision Tree and Random Forest classifiers. The goal is to predict whether a patient has heart disease based on clinical features such as age, cholesterol, blood pressure, etc.

2.Dataset

File: heart.csv
Rows: 1025
Columns: 14 (13 features + 1 target)
Target column: target

1 → Heart disease present

0 → No heart disease

3.Steps Performed

Data Loading & Exploration
checked shape, columns, and missing values.
Train/Test Split
80% training, 20% testing.
Decision Tree Classifier
Trained and visualized the tree.
Controlled overfitting using max_depth.
Random Forest Classifier
Compared accuracy with single Decision Tree.
Feature Importances
Identified most important features.
Cross-Validation
Evaluated model stability.

📊 Results

Decision Tree Accuracy: ~70–75%
Pruned Decision Tree Accuracy: More balanced, less overfitting.
Random Forest Accuracy: ~80–85% (better generalization).
Top Features: cp (chest pain type), thalach (max heart rate), ca (vessels), oldpeak.