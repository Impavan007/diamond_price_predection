import os
import sys
from src.Logger import logging
from src.Exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
class DataIngestion:
    def __init__(self):
        self.ingest_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("src/Notebooks/data/gemstone.csv")
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingest_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingest_config.raw_data_path,index=False)
            logging.info("Train test split initiated")
            train_set,test_set= train_test_split(df,test_size=0.2,random_state=4)
            train_set.to_csv(self.ingest_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingest_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            return (
                self.ingest_config.train_data_path,
                self.ingest_config.test_data_path,
                self.ingest_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys) from e
        finally:
            logging.info("Data ingestion method completed")