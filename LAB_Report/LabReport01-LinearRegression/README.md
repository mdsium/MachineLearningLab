# Diabetes Prediction using Linear Regression


**Lab:** LabReport01 — CSE412-223E2
**Author:** Md. Sium


## Overview
This repository contains the lab report and code for Diabetes Prediction using Linear Regression. The model predicts the `Outcome` by rounding Linear Regression outputs to {0,1}.


## Files
- `data/diabetes.csv` — dataset used.
- `src/linear_regression_model.py` — script version of the notebook.
- `CSE412-223E2-LabReport01-LinearRegression.pdf` — final lab report (PDF).


## Instructions to run
1. Clone the repo.
2. Create a Python environment and install dependencies: `pip install -r requirements.txt` .
3. Run the notebook or script.


## Preprocessing steps



## Results
[Paste evaluation metrics and confusion matrix here after running the code]
## 📐 Model Theory

### 🔸 Hypothesis Function
The Linear Regression hypothesis function predicts the target variable as a linear combination of input features:

\[
\hat{y} = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n
\]

Where:  
- \( \hat{y} \) = predicted output  
- \( x_1, x_2, ..., x_n \) = input features  
- \( \beta_0, \beta_1, ..., \beta_n \) = model coefficients  

---

### 🔸 Cost Function (Mean Squared Error - MSE)
Measures the error between predicted and actual values:

\[
J(\beta) = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2
\]

Where:  
- \( m \) = number of samples  
- \( \hat{y}^{(i)} \) = predicted value  
- \( y^{(i)} \) = actual value  

---

### 🔸 Normal Equation
Used to compute the optimal coefficients analytically:

\[
\beta = (X^T X)^{-1} X^T y
\]

Where:  
- \( X \) = matrix of input features  
- \( y \) = vector of target values  
- \( \beta \) = vector of coefficients  

---

## 📊 Evaluation Metrics

### 1. Accuracy
The proportion of correctly predicted samples:

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

---

### 2. Precision
The proportion of positive predictions that are correct:

\[
\text{Precision} = \frac{TP}{TP + FP}
\]

---

### 3. Recall (Sensitivity)
The proportion of actual positives correctly predicted:

\[
\text{Recall} = \frac{TP}{TP + FN}
\]

---

### 4. F1-Score
Harmonic mean of Precision and Recall:

\[
F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

---

### 5. Confusion Matrix
Represents prediction results:

\[
\begin{bmatrix}
TN & FP \\
FN & TP
\end{bmatrix}
\]

Where:  
- TN = True Negative  
- FP = False Positive  
- FN = False Negative  
- TP = True Positive
