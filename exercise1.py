"""
🔴 Problems:

All logic in one block → not modular.

Hard to reuse functions for other datasets.

No error handling → breaks if column names change.

Not scalable (imagine working on multiple CSVs).

No documentation → not good for collaboration.
"""
### Classroom Activity 
# Exercise 1 - ANSWER #
import logging
import pandas as pd

logging.basicConfig(
    level = logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

def loading_dataset(iris_dataset_url) -> pd.DataFrame:
    '''Read a dataset in the url or the folder path typed by the user.
        Args:
            _None_
        Returns:
            iris_dataframe (pd.DataFrame): Dataset loaded as a dataframe.       
    '''
    try:
        iris_dataframe = pd.read_csv(iris_dataset_url)
        logging.info("Loading the dataset...")
    except:
        logging.critical("Problem to load the dataset.")
    return iris_dataframe

def average_sepal_length(sepal_length_series: pd.Series):
    '''Calculate the average of the sepal length values in the dataset.
        Args:
            sepal_length_series (pd.Series[float]): A series with the sepal_length values.
    '''
    try:
        logging.info(f"\nThe mean value of the sepal length is:\n{sepal_length_series.mean():.2f}")
    except:
        logging.error("Problem to calculate the sepal length average. Verify the function calling and try again.")    

def maximum_petal_width(petal_width_series: pd.Series):
    '''Identify the hightest value in the petal width values in the dataset.

        Args:
            petal_width_series (pd.Series[float]): A series with petal width values.

        Returns:
    '''
    try:
        logging.info(f"The maximun value in the petal width feature is:\n{petal_width_series.max()}")
    except:
        logging.error("Problem to calculate the maximun value of Petal Width feature. Verify the function calling and try again.")

def iris_setosa_filter(iris_dataframe: pd.DataFrame) -> None:
    '''Filter rows where species is "setosa".
        Args:
            iris_dataframe (pd.DataFrame): The iris dataset in a dataframe format.
        Returns:
            iris_setosa_filtered(pd.DataFrame): The rows where species is "setosa".
    '''
    try:
        logging.info(f"\nThe 5 first rows with 'setosa' as iris species are:\n{iris_dataframe[iris_dataframe['species'] == 'setosa'].head()}")
    except:
        logging.error("Problem to filter the iris setosa species. Verify the function calling or the function and try again.")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df_iris = loading_dataset(url)
    average_sepal_length(df_iris['sepal_length'])
    maximum_petal_width(df_iris['petal_width'])
    iris_setosa_filter(df_iris)