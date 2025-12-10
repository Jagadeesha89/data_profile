import pandas as pd 
import numpy as np  
from data_profile.exception.exception import CustomPacakgeException
from data_profile.logging.logger import logging
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import math

class DataReader:
    def __init__(self,data:pd.DataFrame,columns:int=3,y=None,figsize=(10,10),drop_cols:list=[None]):
        self.data=data
        self.y=y
        self.figsize=figsize
        self.columns=columns
        self.drop_cols=drop_cols

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

    def data_charting(self):
        try:
            logging.info("Data charting started")

            # Identify categorical and numeric columns
            cat_columns = [col for col in self.data.columns if self.data[col].dtype == "object"]
            num_columns = [col for col in self.data.columns if self.data[col].dtype != "object"]

            # Remove target variable from both lists (if present)
            if self.y is not None:
                if self.y in cat_columns:
                    cat_columns.remove(self.y)
                if self.y in num_columns:
                    num_columns.remove(self.y)
            
            if self.drop_cols is not None:
                cat_columns=[col for col in cat_columns if col not in self.drop_cols]
                num_columns=[col for col in num_columns if col not in self.drop_cols]

            # -------------------------------
            # Plot numeric columns
            # -------------------------------
            if len(num_columns) > 0:
                plt.figure(figsize=self.figsize)
                plt.suptitle("Univariate Analysis – Numerical Columns",
                            fontsize=20, fontweight="bold", alpha=0.8, y=1.02)

                nrows = math.ceil(len(num_columns) / self.columns)

                for i, col in enumerate(num_columns):
                    plt.subplot(nrows, self.columns, i + 1)
                    sns.histplot(self.data[col], bins=30)
                    plt.xlabel(col)

                plt.tight_layout()
                plt.show()
            else:
                logging.info("No numerical columns available for charting.")

            # -------------------------------
            # Plot categorical columns
            # -------------------------------
            if len(cat_columns) > 0:
                plt.figure(figsize=self.figsize)
                plt.suptitle("Univariate Analysis – Categorical Columns",
                            fontsize=20, fontweight="bold", alpha=0.8, y=1.02)

                nrows = math.ceil(len(cat_columns) / self.columns)

                for i, col in enumerate(cat_columns):
                    plt.subplot(nrows, self.columns, i + 1)
                    sns.countplot(x=self.data[col])
                    plt.xlabel(col)
                    plt.xticks(rotation=45)

                plt.tight_layout()
                plt.show()
            else:
                logging.info("No categorical columns available for charting.")

        except Exception as e:
            raise CustomPacakgeException(e, sys)
            