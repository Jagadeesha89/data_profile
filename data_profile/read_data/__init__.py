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
            list_items=[]
            for col in self.data.columns:
                list_items.append([col,self.data[col].dtype,self.data[col].isna().sum(),100*self.data[col].isna().sum()/len(self.data[col]),
                self.data[col].nunique(),self.data[col].unique()[:4]])
            summ_df=pd.DataFrame(data=list_items,columns="Features Data_type Null_Num Null_Pct Unique_no. Top4_unique_value".split())
            logging.info("Data summary completed")
            print("\n")
            print("Data summary:")
            print(f"The Data consist of {len(self.data)} rows and {len(self.data.columns)} columns \n Total Categorical features are {len(self.data.select_dtypes(include=[object]).columns)} \n Total Numerical features are {len(self.data.select_dtypes(include=[np.number]).columns)}")
            print("\n")
            print(summ_df)
        except Exception as e:
            raise CustomPacakgeException(e,sys) 