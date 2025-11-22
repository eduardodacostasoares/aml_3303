# **ASSIGNMENT 2**

## **1. Project overview and objectives**
- Many Airbnb hosts struggle to choose a competitive and realistic nightly price for new listings, especially in large cities with diverse neighbourhoods and property types.  

- This project aims to:

    - Build a **clean, reusable data pipeline** from **AWS S3 → Pandas → Scikit-learn → MLflow**.
    - Handle **noisy real-world data** (missing values, outliers, categorical variables).
    - Train and compare multiple **regression models** to predict nightly prices.
    - Use **MLflow** to track all experiments and **register the best model** for future deployment.

---
### **1.1.** *Dataset*
- The dataset used is _AB_NYC_2019.csv_ that contains 16 features (including the target variable _price_):

    |  Column Name |	Data Type |	Description |
    |---|---|---|
    |_id_	| Integer	| Unique identifier for each listing
    |_name_ |	String	| Name of the listing
    |_host_id_ |	Integer	| Unique identifier for the host
    |_host_name_ |	String	| Name of the host
    |_neighbourhood_group_ |	Categorical	| Broad region in NYC where the listing is located
    |_neighbourhood_	| Categorical |	Specific neighborhood within the region
    |_latitude_	| Float	| Latitude coordinate of the listing
    |_longitude_	| Float	| Longitude coordinate of the listing
    |_room_type_	| Categorical |	Type of rental offered
    |_**price**_	| Integer (**target**)	| Price per night in USD
    |_minimum_nights_	| Integer |	Minimum number of nights for booking
    |_number_of_reviews_	| Integer |	Total number of reviews for the listing
    |_last_review_	| Date |	Date of the most recent review
    |_reviews_per_month_ |	Float	| Average number of reviews per month
    |_calculated_host_listings_count_ |	Integer | Number of listings the host has
    |_availability_365_ |	Integer	| Number of days the listing is available per year


## **2. Setup and execution instructions.**
### **2.1** Steps:
#### **2.2** Clone repository
```
git clone https://github.com/eduardodacostasoares/aml_3303.git
cd assignment2
```
#### **2.3** Create and activate virtual environment
**Creating**
```
python -m venv .venv
```
**Activating**
- **Windows Powershell**
    ```
    .venv\Scripts\Activate.ps1
    ```

- **macOS**/**Linux**
    ```
    source .venv/bin/activate
    ```
    
#### **2.4** Installing dependencies
```
pip install -e .
```

#### **2.5.** Configuring AWS and MLflow
- Create an `.env` file:
```
AB_NYC_BUCKET=<name_of_the_bucket>
AB_NYC_KEY=data/AB_NYC_2019.csv
MLFLOW_TRACKING_URI=sqlite:///mlflow.db

```
- Confirm your AWS credentials:
```
~/.aws/credentials
```


Before to start the exploratory data anlysis (*EDA*), by security reasons and by efficiency, all the columns with *identifiers* and/or *personal information* will be **dropped**.

The *key features* in the dataset are:
Key fields:

- **Location**
  - `neighbourhood_group` (Manhattan, Brooklyn, Queens, Bronx, Staten Island)
  - `neighbourhood` (fine-grained areas)
  - `latitude`, `longitude`
- **Listing characteristics**
  - `room_type` (Entire home/apt, Private room, etc.)
  - `minimum_nights`
- **Demand & activity**
  - `number_of_reviews`
  - `last_review`
  - `reviews_per_month`
  - `availability_365`
- **Host info**
  - `calculated_host_listings_count`
- **Target variable**
  - `price` (nightly listing price in USD) 

<br></br>
The **figures 1** and **2**, shows a description and a visualization of the numerical values in the dataset, revealing that almost all numerical features has *outliers*. 

<br></br>
!["Description of all numerical features"](images\2_1_describe.png)
**Fig. 1.** Description of numerical features.

<br></br>
!["Histplot of all features"](images\2_2_histogram_all.png)
**Fig. 2.** Distribution of all features. Outliers can be detected in almost all features


## **3. Repository structure and workflow description.**
```text
.
├── images/
│    ├── 1_create_a_bucket.png      # S3 bucket created
│    ├── 2_1_describe.png           # Description of the dataset
|    ├── 2_2_histogram.png          # Distribution of each feature in the dataset
|    ├── histogram_price.png        # Distribution of target variable
|    ├── top10_gbr.png         
│    ├── top10_rf.png               # Top 10 important features by Random Forest
|    ├── train_test.png             # Training and test metric results
│    └── val.png                    # Validation metrics results
├── src/
│    ├── main_notebook.ipynb        # Main training & MLflow pipeline script
|    └── send_dataset_bucket.py     # Saving the dataset in the S3 Bucket
├── pyproject.toml                  # Dependencies & project config
├── README.md                       # This file
├── uv.lock                         # high-level version of pyproject.toml
└── .env                            # Environment variables
```
<br></br>

### *WORKFLOW*
### 1. Load Data from AWS S3
- Configure S3 bucket and file path.
- Use boto3 to download CSV to memory and load into pandas.

### 2. Data Preprocessing
##### 2.1 Initial Cleaning
- Drop non-informative ID columns.
- Inspect dataset with info() and describe().

##### 2.2 Feature Engineering
- Convert `last_review` to `days_since_last_review`.
- Clean review metrics.
- Handle outliers via IQR winsorization.
- Apply log transforms to skewed features.

#### 3. Splitting Data
- Split into Train/Validation/Test (60/20/20).
- Separate X and y.

#### 4. Preprocessing
- Scale numeric features with StandardScaler.
- OneHotEncode categorical features.
- Combine into final matrices: X_train_final, X_val_final, X_test_final.

#### 5. Model Training
- Train Linear Regression, Random Forest, Gradient Boosting.
- Evaluate using RMSE and R² on val & test sets.
- Random Search for RF and GBR hyperparameters.

#### 6. MLflow Experiment Tracking
- Set experiment name and tracking URI.
- For each model:
  - Start run, log params, log metrics.
  - Log model with signature + input_example.
- Determine best model from validation RMSE.

#### 7. Model Registry
- Register best-performing model in MLflow Model Registry.

#### 8. MLflow UI Inspection
- Launch UI with: `mlflow ui --backend-store-uri mlruns --port 5000`
- Screenshot:
  - Experiment runs
  - Run details
  - Registered model

#### 9. Model Comparison
- Compare LR, RF, GBR using validation/test RMSE and R².
- Present table & reasoning.

## **4. Screenshots of MLflow UI showing experiment runs, metrics, and model registry.**
- After logging all experiments to MLflow, by the validation RMSE and registered it in the MLflow Model Registry under the name airbnb_nyc_price_model_manual_preproc. This allows versioned management of models, making it easy to promote the best model to production and compare future versions.

!["Train and test metrics results"](images\train_test.png)
**Fig. 3.** *Root Mean Squared Error*, *R2 Score* and *Mean Squared Error* of each one of the models, in training and test. 

<br></br>

!["Validation metrics results"](images\val.png)
**Fig. 4.** *Root Mean Squared Error*, *R2 Score* and *Mean Squared Error* of each one of the models (validation). 

- All the models showed some signals of overfitting (with a difference between the results in training stage and validation/test stage).

## **5. Key insights and observations.**

!["Top 10 most important features in Random Forest"](images\top10_rf.png)

**Fig. 5.** Top 10 most important features in **Random Forest**.

<br></br>

!["Top 10 most important features in Gradient Boosting Regressor"](images\top10_gbr.png)

**Fig. 6.** Top 10 most important features in **Gradient Boosting Regressor**
<br></br>

- In the the non-linear models (*RF* and *GBR*), *Price* cannot be _perfectly_ explained by these features since there are a lack of other variables, like "pictures of the place", "host quality", "turistic points near" or "events near" and other features.

- There are features in this dataset that are highly skewed (minimum_nights, availability_365, reviews_per_month, number_of_reviews). Even after wensorization and log transformation the skewness remained. This characteristic is showed to be natural of the data (e.g. most bookings are short stays), so trying to normalize this data can remove the meaningful information.

- The top 3 features indicates that **location** (*latitude* and *longitude*) and the **room type** (of course, the entire home) are the most important features to guide the price (the other features has not so much importance).