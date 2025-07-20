import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from src.Logger import logging
from src.Exception import CustomException
from src.utils import save_object, evaluate_model
from sklearn.tree import DecisionTreeRegressor
from dataclasses import dataclass
import sys
import os

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting depndent and independent data')
            X_train,y_train,X_test,y_test= (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            Models={
                'LinearRegression':LinearRegression(),
                'Ridge':Ridge(),
                "Lasso":Lasso(),
                "ElasticNet":ElasticNet(),
                'DecisionTreeRegressor':DecisionTreeRegressor()
            }
            model_report: dict=evaluate_model(X_train,y_train,X_test,y_test,Models)
            print(model_report)
            print('\n=====================================================================')
            logging.info(f'Model Report : {model_report}')
            best_model_score=max(sorted(model_report.values()))
            best_model_name= list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=Models[best_model_name]
            print(f"best model is {best_model_name}")
            logging.info(f'best model name is{best_model}')
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)




        except Exception as e:
            raise CustomException(e, sys)


