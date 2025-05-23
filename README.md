# Housing Price Predictor

A machine learning project designed to predict housing prices based on a variety of features. This project leverages several regression models to deliver accurate and explainable predictions, making it ideal for educational, experimental, or real-world applications.

## Features

* **Data Preprocessing & Feature Engineering**
  Comprehensive pipeline for cleaning data and transforming features to improve model performance.

* **Multiple Regression Models**

  * Linear Regression
  * Random Forest Regressor
  * *(Easily extensible to include models like Gradient Boosting, XGBoost, etc.)*

* **Model Evaluation**
  Models are assessed using robust metrics:

  * **R² (Coefficient of Determination)**

* **Model Exporting**
  Trained models are saved as `.pkl` files for easy reuse and deployment.

## Model Performance

| Model             | MAE    | RMSE   | R²   |
| ----------------- | ------ | ------ | ---- |
| Linear Regression | 23,452 | 31,290 | 0.64 |
| Random Forest     | 18,421 | 24,839 | 0.82 |

> 📌 *Note: Metrics are based on sample data. Actual results may vary depending on dataset and preprocessing.*
