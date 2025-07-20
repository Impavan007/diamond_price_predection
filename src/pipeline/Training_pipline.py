import os
import sys


import pandas as pd

from src.components.Data_ingestion import DataIngestion
from src.components.Data_transformation import DataTransformation
from src.components.Model_trainer import ModelTrainer
from src.Logger import logging

if __name__ == "__main__":
    obj = DataIngestion()
    
    train_data_path, test_data_path, raw_data_path = obj.initiate_data_ingestion()
    print(f"Train data path: {train_data_path}")
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_path=train_data_path, test_path=test_data_path)
    logging.info(f"Train data path: {train_data_path}")
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)
