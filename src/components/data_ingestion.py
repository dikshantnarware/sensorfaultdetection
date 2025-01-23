import sys#module to get the system specific parameters and functions
import os#module to interact with the operating system
import numpy as np#module to work with arrays
import pandas as pd#module to work with dataframes
from pymongo import MongoClient#module to interact with mongodb
from zipfile import Path#module to work with zip files
from src.constant import *#importing all the constants from the constant file
from src.exception import CustomException#custom exception class
from src.logger import logging#module to log the information of the application
from src.utils.main_utils import MainUtils# module to work with the utility functions
from dataclasses import dataclass#  module to work with dataclasses




@dataclass#decorator to create a dataclass
class DataIngestionConfig:#class to store the data ingestion configuration
    artifact_folder: str = os.path.join(artifact_folder)#path to store the artifacts of the data ingestion components
    
        

class DataIngestion:#class to perform the data ingestion operations
    def __init__(self):#constructor to initialize the data ingestion components
        
        self.data_ingestion_config = DataIngestionConfig()#initializing the data ingestion configuration
        self.utils = MainUtils()#initializing the MainUtils class


    def export_collection_as_dataframe(self,collection_name, db_name):# method to export the collection as a dataframe
        try:#   method to export the collection as a dataframe
            mongo_client = MongoClient(MONGO_DB_URL)#   connecting to the mongodb

            collection = mongo_client[db_name][collection_name]#   getting the collection from the database

            df = pd.DataFrame(list(collection.find()))#converting the collection to a dataframe

            if "_id" in df.columns.to_list():#checking if the _id column is present in the dataframe
                df = df.drop(columns=["_id"], axis=1)#dropping the _id column from the dataframe

            df.replace({"na": np.nan}, inplace=True)#replacing the na values with nan in the dataframe

            return df#returning the dataframe

        except Exception as e:#handling the exception
            raise CustomException(e, sys)#raising the custom exception

        
    def export_data_into_feature_store_file_path(self)->pd.DataFrame:#method to export the data into the feature store file path
        """
        Method Name :   export_data_into_feature_store
        Description :   This method reads data from mongodb and saves it into artifacts. 
        
        Output      :   dataset is returned as a pd.DataFrame
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   0.1
       
        """
        try:#method to export the data into the feature store file path
            logging.info(f"Exporting data from mongodb")#logging the information
            raw_file_path  = self.data_ingestion_config.artifact_folder# getting the raw file path
            os.makedirs(raw_file_path,exist_ok=True)#creating the directory for the raw file path

            sensor_data = self.export_collection_as_dataframe(#exporting the collection as a dataframe
                                                              collection_name= MONGO_COLLECTION_NAME,#  collection name
                                                              db_name = MONGO_DATABASE_NAME)#  database name            

            logging.info(f"Saving exported data into feature store file path: {raw_file_path}")#logging the information
        
            feature_store_file_path = os.path.join(raw_file_path,'wafer_fault.csv')#getting the feature store file path
            sensor_data.to_csv(feature_store_file_path,index=False)#saving the sensor data into the feature store file path
           

            return feature_store_file_path#returning the feature store file path
            

        except Exception as e:#handling the exception
            raise CustomException(e,sys)#raising the custom exception

    def initiate_data_ingestion(self) -> Path:# 
        """
            Method Name :   initiate_data_ingestion
            Description :   This method initiates the data ingestion components of training pipeline 
            
            Output      :   train set and test set are returned as the artifacts of data ingestion components
            On Failure  :   Write an exception log and then raise an exception
            
            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")#logging the information

        try:#  handling the exception
            
            feature_store_file_path = self.export_data_into_feature_store_file_path()#exporting the data into the feature store file path

            logging.info("Got the data from mongodb")#  


            logging.info(#  logging the information
                "Exited initiate_data_ingestion method of Data_Ingestion class"#logging the information
            )#logging the information
            
            return feature_store_file_path#returning the feature store file path

        except Exception as e:#  handling the exception
            raise CustomException(e, sys) from e#raising the custom exception
