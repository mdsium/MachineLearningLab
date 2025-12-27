# Bangladeshi News Classification using Naive Bayes

## Project Overview
This repository contains a binary text classification project that uses **Naive Bayes** to classify Bangladeshi news headlines and descriptions into two categories: **Politics** and **Sports**.

The dataset consists of 100 real news samples (50 politics, 50 sports) collected from major Bangladeshi newspapers and international sources reporting on Bangladesh, reflecting events around late December 2025 (e.g., Tarique Rahman's return, BPL 2025-26 cricket tournament).

The Jupyter notebook demonstrates a complete machine learning pipeline:
- Data loading and exploration
- Text preprocessing (lowercase, punctuation/number removal, stopword removal, lemmatization)
- Feature extraction
- Train-test split
- Naive Bayes model training
- Evaluation with accuracy and confusion matrix
- Optional visualization using PCA and seaborn

## Repository Files

- **`News_data_set.csv`**  
  The main dataset with 100 rows and 3 columns:
  - `title`: News headline
  - `description`: Short news description
  - `label`: Category (`politics` or `sports`)

  Example:
  ```csv
  title,description,label
  Tarique Rahman Returns After 17 Years in Exile,"BNP acting chairman Tarique Rahman arrives in Dhaka from London, greeted by massive crowds ahead of February elections.",politics
  BPL 2025-26 Kicks Off in Sylhet,"Season starts with Sylhet Titans vs Rajshahi Warriors amid organizational challenges.",sports
## Files in this Repository

| File                  | Description |
|-----------------------|-------------|
| `News_data_set.csv`   | The News_data_set |
| `CSE412_223E2_LabReport03_NaïveBayes.ipynb` | full implementation, preprocessing, training, and evaluation |
| `README.md`           | This file |

