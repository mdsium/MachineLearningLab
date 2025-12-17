# Iris Flower Classification with K-Nearest Neighbors (KNN)

This repository contains a complete implementation of the classic Iris flower classification problem using the **K-Nearest Neighbors (KNN)** algorithm. The project explores data preprocessing, model training, hyperparameter tuning, and performance evaluation across different train-test split ratios and values of *k*.

## Project Overview

- Dataset: Iris (150 samples, 4 features, 3 classes)
- Preprocessing: Min-Max scaling, no missing values
- Model: KNN (from scratch)
- Hyperparameters tested: k = 1, 3, 5, 7, 9, 11, 13, 15
- Train-test splits: 50:50, 60:40, 70:30, 80:20
- Metrics: Accuracy, Precision, Recall, F1-score (macro), Confusion Matrix
- Best performance: **97.78% accuracy** (70:30 split, k=7 to 15)

## Dataset

The Iris dataset is a well-known benchmark in machine learning, containing 150 samples from three Iris species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

Each sample has 4 numerical features:
- sepal_length (cm)
- sepal_width (cm)
- petal_length (cm)
- petal_width (cm)

The dataset is perfectly balanced (50 samples per class) with no missing values.

## Project Goals

- Preprocess the data (Min-Max scaling)
- Split the dataset into train/test sets using multiple ratios: 50:50, 60:40, 70:30, 80:20
- Train KNN models with varying *k* values (1, 3, 5, 7, 9, 11, 13, 15)
- Evaluate performance using accuracy, precision, recall, F1-score, and confusion matrix
- Identify the optimal *k* and split ratio

## Results Summary

The KNN classifier achieves near-perfect performance on the Iris dataset, with the best results on the 70:30 split.

| Train:Test Ratio | Best k | Accuracy | Macro F1-Score | Notes |
|------------------|--------|----------|----------------|-------|
| 50:50            | 7–9    | 97.33%   | 0.9753         | Minor misclassifications between versicolor & virginica |
| 60:40            | 7–11   | 96.67%   | 0.9702         | Consistent high performance |
| 70:30            | 7–15   | 97.78%   | 0.9810         | **Optimal** – excellent generalization |
| 80:20            | 9–15   | 96.67%   | 0.9710         | Very reliable but smaller test set |

**Optimal configuration**: 70:30 split with *k* = 7 (or any odd value from 7–15)

Misclassifications occur only between *Iris-versicolor* and *Iris-virginica* (setosa is always perfectly classified).

## Files in this Repository

| File                  | Description |
|-----------------------|-------------|
| `iris.csv`            | The Iris dataset (included) |
| `knn_iris_classification.ipynb` | full implementation, preprocessing, training, and evaluation |
| `README.md`           | This file |

