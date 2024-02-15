# Employee Promotion Prediction Project

## Overview

This project aims to predict whether an employee will be promoted or not based on various features such as department, education, gender, recruitment channel, and more. 

## Dataset

The dataset used for this project contains the following columns:

- `employee_id`: Unique identifier for each employee.
- `department`: The department to which the employee belongs.
- `region`: The region where the employee is located.
- `education`: The education level of the employee.
- `gender`: The gender of the employee.
- `recruitment_channel`: The channel through which the employee was recruited.
- `no_of_trainings`: Number of training programs attended by the employee.
- `age`: Age of the employee.
- `previous_year_rating`: Rating received by the employee in the previous year.
- `length_of_service`: Length of service of the employee.
- `awards_won`: Whether the employee has won any awards (binary: 0 or 1).
- `avg_training_score`: Average training score received by the employee.
- `is_promoted`: The target variable indicating whether the employee was promoted (binary: 0 or 1).

## Key Insights

- **Maximum number of trainings:** 1.
- **Maximum age of employees:** 30 to 35 years.
- **Most common previous year rating:** 3.0 to 3.5.
- **Maximum length of service:** 5 years.
- **Maximum awards won:** 0.
- **Average training score:** Ranges from 45 to 72 out of 100.

- **Department Insights:**
  - Sales and Marketing department has the maximum number of employees.
  - Technology department employees have the highest chance of getting promoted.

- **Education Insights:**
  - Most employees hold a Bachelor's degree.
  - Employees with a master's degree or above have the highest chance of getting promoted.

- **Gender Insights:**
  - Male employees outnumber females.
  - Female employees have a higher chance of getting promoted.

- **Recruitment Channel Insights:**
  - The most common recruitment channel is 'Other'.
  - Employees with referral as the recruitment channel have the highest chance of getting promoted.

- **Promotion by Department:**
  - Sales and Marketing department has a high chance of promotion.

- **Random Forest Classifier Accuracy: 0.9429822560780915**
- **KNN Classifier Accuracy: 0.9345436299776491**
- **SVC Classifier Accuracy: 0.9142453131414496**
- **Decision Tree Classifier Accuracy: 0.9429822560780945**
- **Logistic Regression Classifier Accuracy: 0.9175523422889204**

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- Required Python packages (specified in `requirements.txt`). Install them using: `pip install -r requirements.txt`.

## References

- [Scikit-learn documentation](https://scikit-learn.org/stable/documentation.html) for machine learning models and preprocessing.
