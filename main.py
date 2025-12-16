from data_profile.logging.logger import logging
from data_profile.exception.exception import CustomPacakgeException
import sys
from data_profile import DataReader
import pandas as pd


if __name__ == "__main__":
    try:
        logging.info("First logging started")
        data_path="D:\python_packages\Jan_23_rev.csv"
        logging.info("Reading data Started")
        df=pd.read_csv(data_path)
        data_sum=DataReader(df,y="Status",drop_cols=["Acc","Status"],cat_col_chart="countplot",num_col_chart="boxplot",columns=4,figsize=(14,7))
        df_1=data_sum.data_summary()
        print(df_1)
        logging.info("Data summary completed")
        data_sum.data_charting()
    except Exception as e:
        logging.info("error occured")
        raise CustomPacakgeException(e, sys)


