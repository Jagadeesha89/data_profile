from data_profile.logging.logger import logging
from data_profile.exception.exception import CustomPacakgeException
import sys
from data_profile.read_data import DataReader
import pandas as pd


if __name__ == "__main__":
    try:
        logging.info("First logging started")
        data_path="./synthetic_online_retail_data.csv"
        logging.info("Reading data Started")
        df=pd.read_csv(data_path)
        data_sum=DataReader(df)
        data_sum.data_summary()
        logging.info("Data summary completed")
    except Exception as e:
        logging.info("error occured")
        raise CustomPacakgeException(e, sys)

