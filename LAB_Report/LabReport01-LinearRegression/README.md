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

1. **Handle Missing/Zero Values**  
   Replace all zero values in the following features with the **median** of their respective column:
   - Glucose
   - BloodPressure
   - SkinThickness
   - Insulin
   - BMI

2. **Special Glucose Handling**  
   - Replace the **first row’s Glucose value** with the **maximum** glucose value in the dataset.  
   - For **all records with the minimum Age**, replace their Glucose values with the **minimum** glucose value in the dataset.

3. **Feature Scaling**  
   Apply **StandardScaler** to all features to normalize the data.

4. **Train/Test Split**  
   - Training set: 80% of data  
   - Testing set: 20% of data  
   - `random_state = 42` ensures reproducibility

---

## 🤖 Model Used
**Linear Regression** from `sklearn` is used to predict diabetes probability.

### Post-processing of predictions
```python
import numpy as np

# Convert regression outputs to binary classes
y_pred = np.round(predictions)
y_pred = np.clip(y_pred, 0, 1)  # Ensures values are 0 or 1


## Results

Accuracy: 0.7597402597402597
Precision: 0.68
Recall: 0.6181818181818182
F1-score: 0.6476190476190476
Confusion Matrix:
 [[83 16]
 [21 34]]