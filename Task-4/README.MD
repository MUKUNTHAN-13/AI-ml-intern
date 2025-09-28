Logistic Regression on Breast Cancer Dataset

This project applies Logistic Regression to the Breast Cancer Wisconsin dataset (data.csv) to classify tumors as:

1.Overview

M (Malignant → 1)
B (Benign → 0)

2.Libraries

pandas
numpy
scikit-learn
matplotlib

3.Steps

Load dataset and clean (drop id, unnamed columns).
Encode target: M → 1, B → 0.
Split into train/test sets.
Standardize features.
Train Logistic Regression model.
Evaluate with:
Confusion Matrix
Precision, Recall, F1
ROC-AUC & ROC Curve
Tune threshold (default 0.5 → try 0.3, 0.7).