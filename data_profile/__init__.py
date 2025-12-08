import pandas as pd 
import numpy as np  
from data_profile.exception.exception import CustomPacakgeException
from data_profile.logging.logger import logging
import sys

class DataReader:
    def __init__(self,data:pd.DataFrame):
        self.data=data

    def data_summary(self):

        try:
            logging.info("Data summary started")
            summ_df=pd.DataFrame(
                [
                    [col,
                    self.data[col].dtype,
                    self.data[col].isna().sum(),
                    100*self.data[col].isna().sum()/len(self.data[col]),
                    self.data[col].nunique(),
                    self.data[col].unique()[:4],
                    ]
                    for col in self.data.columns
                ],
                columns=[
                    "Column",
                    "Data Type",
                    "Null Count",
                    "Null Percentage",
                    "Unique Count",
                    "Unique Values",    
                ]
            )
            return summ_df

        except Exception as e:
            raise CustomPacakgeException(e,sys) 