<h1>Employee Churn Prediction at TechNova Solutions</h1>

<h2>1. Context</h2>

TechNova Solutions, a mid-sized IT services company with approximately 1,200 employees, is experiencing a significantly higher employee attrition rate compared to industry standards. This high turnover leads to increased costs (recruitment, training), project delays, and reduced overall employee satisfaction.

<h2>2. Problem Statement</h2>

The company lacks a systematic method to identify employees likely to leave before they resign, resulting in reactive and inefficient retention efforts. The goal is to build a predictive solution and provide explainable insights to HR to enable proactive retention interventions, prioritize efforts, and measure impact.
<br>
<h2>3. Objective</h2>

- Identify key factors influencing employee attrition.
- Build a machine learning model to classify employees as "likely to leave" or "likely to stay."
- Provide actionable insights and recommendations to the HR department.
- (Future) Integrate the model into the HR system for continuous monitoring.
<br>
</h2>4. Data Understanding</h2>

The dataset contains various features related to employee demographics, history, performance, and HR data, including:
- **Demographics:** Age, Gender, Marital Status
- **Employee History:** Tenure, Department, Job Role, Salary
- **Performance Metrics:** Performance Rating, Promotions, Training Hours, Projects Completed
- **HR Data:** Overtime Hours, Satisfaction Level, Work-Life Balance, Average Monthly Hours Worked, Absenteeism, Distance from Home, Manager Feedback Score
- **Target Variable:** Churn (0: No Churn, 1: Churn)

Initial data checks revealed no missing values or duplicate rows. The 'Employee ID' was removed for privacy and irrelevance to the model.
<br>
<h2>5. Exploratory Data Analysis (EDA)</h2>

EDA involved analyzing the distribution of individual features and their relationship with the target variable 'Churn'.
- **Categorical Features:** Summary statistics and cross-tabulations with 'Churn' were examined to understand churn rates across different categories (e.g., Department, Job Role, Work Location, Marital Status, Gender). Notable findings included potentially higher churn in specific combinations like Divorced females in Hybrid work locations.
- **Numerical Features:** Descriptive statistics, histograms (with binning for clarity), and box plots were used to understand the distributions, central tendencies, spread, and potential outliers. A heatmap of numerical feature correlations showed no extremely strong linear correlations with 'Churn', suggesting a complex interplay of factors influences churn.
<br>
<h2>6. Feature Engineering</h2>

To potentially improve model performance by capturing more complex relationships, new features were engineered:
- Ratios like 'Overtime\_Ratio', 'Training\_Intensity', and 'Project\_Load'.
- A 'Burnout\_Index' combining overtime and satisfaction.
- 'Relative\_Salary' comparing an employee's salary to their department's average.
The original features used to create these new features were dropped to avoid redundancy. Correlation analysis of the new features with 'Churn' showed weak linear relationships, suggesting their value might lie in non-linear interactions captured by certain models.
<br>
<h2>7. Experiment Design</h2>

- **Models:** Logistic Regression (as a baseline and for interpretability) and Random Forest (for non-linear interactions and robustness) were chosen.
- **Data Splitting:** The data was split into 80% training and 20% testing using stratified sampling to maintain the churn rate distribution.
- **Class Imbalance:** SMOTE (Synthetic Minority Over-sampling Technique) was applied to the training data to oversample the minority class (Churn) and mitigate imbalance.
- **Evaluation Metric:** **Recall** was prioritized as the primary evaluation metric, as the business goal is to identify as many employees likely to leave as possible (minimize False Negatives) to allow for proactive interventions. Other metrics like Accuracy, Precision, F1-Score, and ROC AUC were also considered.
- **Validation:** 5-fold cross-validation was applied during hyperparameter tuning on the training set.
<br>
<h2>8. Model Training and Evaluation</h2>

Both Logistic Regression and Random Forest models were trained on the engineered training data after applying SMOTE and hyperparameter tuned using Grid Search with 'recall' as the scoring metric. Their performance was evaluated on the unseen engineered test data.

- **Logistic Regression (Engineered + SMOTE):** The model was trained, and Grid Search optimized for recall. Evaluation metrics on the test set were calculated and displayed. The initial low recall with the default threshold highlighted the need for threshold tuning.
- **Random Forest (Engineered + SMOTE):** The model was trained, and Grid Search optimized for recall. Evaluation metrics on the test set were calculated and displayed.

<h2>9. Recommendations</h2>
The HR team can develop a strategy to hold people in management positions, with PhD (e.g. improve in the benefits, since they are most experienced and with a stressful activities)

The "hybrid" system demonstrated "worst" results with people with *excellent* work-life balance (possibility to change them to remote or on-site), **so** a probably solution is analyze each one of this employees with *excellent* work-life balance and change them to *remote* or *on-site*, depending of their performance.

Divorced women and people from other gender are highly likely to leave the company (HR must investigate what are causing this behaviour) when work in hybrid (On-site and Remote) system.