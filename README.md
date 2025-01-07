# COVID-19 Data Analysis and Prediction

## **Overview**
This project is part of the "Introduction to Data Science" course and focuses on analyzing and modeling COVID-19 data using various data science techniques. The project demonstrates skills in Exploratory Data Analysis (EDA), data preprocessing, and machine learning. The main dataset used for the analysis is the `covid_19_clean_complete.csv`, which provides global COVID-19 records.

---

## **Objectives**
1. Perform Exploratory Data Analysis (EDA) with at least 10-15 different analyses.
2. Preprocess the dataset for machine learning purposes.
3. Apply supervised machine learning models to make predictions based on the data.
4. Evaluate the performance of the models and compare their effectiveness.

---

## **Dataset**
### **Dataset Name:**
`covid_19_clean_complete.csv`

### **Dataset Source:**
This dataset contains global COVID-19 records, including:
- Confirmed cases
- Deaths
- Recovered cases
- Active cases

The dataset includes sufficient features and records to perform meaningful analysis.

### **Files in Dataset:**
The dataset zip file contains:
- `country_wise_latest.csv`
- `covid_19_clean_complete.csv`
- `day_wise.csv`
- `full_grouped.csv`
- `usa_county_wise.csv`
- `worldometer_data.csv`

---

## **Steps Completed in the Project**

### **1. Exploratory Data Analysis (EDA)**
- Summary statistics (mean, median, mode).
- Correlation analysis and heatmap visualization.
- Pairwise relationships between features.
- Visualization of feature distributions.

### **2. Data Preprocessing**
- Handled missing values using `SimpleImputer`.
- Scaled numerical features using `StandardScaler`.
- Selected relevant features for modeling.
- Split the data into training and testing sets.

### **3. Machine Learning Models**
#### **Models Applied:**
- **Linear Regression**: A simple regression model to predict the number of confirmed cases.
- **Random Forest Regression**: A more robust model to handle complex feature relationships.

#### **Model Evaluation Metrics:**
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- \(R^2\) Score

### **4. Visualizations**
- Correlation heatmaps.
- Comparison of model performance metrics.
- Feature importance analysis (Random Forest).

---

## **Results and Insights**
- Random Forest performed better than Linear Regression in terms of all evaluation metrics.
- The correlation heatmap revealed strong relationships between certain features like deaths, recoveries, and confirmed cases.
- Feature importance analysis highlighted the key predictors for confirmed cases.

---

## **How to Use This Repository**
### **1. Clone the Repository:**
```
git clone https://github.com/username/covid19-analysis.git
cd covid19-analysis
```

### **2. Install Dependencies:**
Ensure you have Python installed. Then, install the required libraries:
```
pip install -r requirements.txt
```

### **3. Run the Notebook:**
Use Jupyter Notebook or any Python IDE to run the notebook file:
```
jupyter notebook covid-19-dataset.ipynb
```

### **4. Dataset Location:**
Place the dataset files in the appropriate folder (as referenced in the notebook).

---

## **Future Improvements**
- Expand the EDA section to include outlier detection and grouped aggregations.
- Experiment with hyperparameter tuning for the Random Forest model.
- Add more machine learning models, such as Gradient Boosting or XGBoost.
- Develop an interactive web application using Streamlit.

---

## **Technologies Used**
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## **Contributors**
- **Fatima Mubasher** - Data Scientist

Feel free to fork this repository and contribute by submitting pull requests!

