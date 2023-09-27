# Machine Learning Training Pipeline Readme

This README file provides an overview of the training pipeline for the machine learning algorithm using Azure ML Designer. The pipeline aims to build a predictive model using logistic regression to classify data with a focus on high recall and precision rates. Here are the steps involved in the pipeline:

1. Dataset Description

The dataset used for this machine learning task contains 14 features. The goal is to predict a binary outcome based on these features.

2. Feature Selection

To improve model performance and reduce dimensionality, we remove two high cardinality features: product_id and uid.

3. Data Preprocessing

a. Remove Null Values: Any rows with missing values are removed from the dataset.

b. Remove Duplicate Values: Duplicate rows in the dataset are identified and removed to ensure data quality.

4. Feature Engineering

A feature engineering method is applied to calculate the "power" of certain features, which can enhance the predictive power of the model.

5. One-Hot Encoding

The categorical column "type" is one-hot encoded to convert it into a numerical format, allowing the model to use it effectively.

6. Data Normalization

The data is normalized to ensure that all features are on the same scale. This step is important for models like logistic regression.

7. Data Split

The dataset is divided into two parts: a training set (80%) and a test set (20%) for model evaluation.

8. Model Training

Logistic regression is used as the machine learning algorithm for this task. The Synthetic Minority Over-sampling Technique (SMOTE) is applied to address the class imbalance issue, as mentioned in the problem statement.

9. Model Evaluation

The trained logistic regression model is evaluated on the test dataset to assess its performance. The model's performance metrics include:

Recall: Achieving a high recall is crucial for identifying as many true positives as possible.

Precision: Achieving a high precision is important to minimize false positives.

Other metrics like accuracy, F1-score, and AUC-ROC may also be considered based on the specific requirements of the problem.

## Model Performance

The trained model yields a recall rate of 97% and a precision rate of 100%, indicating its effectiveness in identifying relevant cases while minimizing false positives.

## Azure ML Designer

This training pipeline is designed and executed using Azure ML Designer, which provides a user-friendly interface for building and deploying machine learning pipelines on the Azure platform.