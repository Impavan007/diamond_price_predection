import pickle
import os
import sys
from src.Logger import logging
from src.Exception import CustomException
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_absolute_error

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(e, sys) from e

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report ={}
        for i in range(len(models)):
            model= list(models.values())[i]
            model.fit(X_train,y_train)
            y_test_pred=model.predict(X_test)
            test_model_score= r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]= test_model_score
        return report

    except Exception as e:
        logging.info("Exception occured in evaluation")
        raise CustomException(e,sys)
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:

        logging.info(f"Exception occured in load_object")
        raise CustomException(e,sys)
    