import os,sys
from src.constant import *
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.utils import get_table_as_dataframe
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):     
        try:
            logging.info(f"{'>>'*20} Data Extraction Started......{'<<'*20} \n\n")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys) from e

    def get_data_from_mysql(self):
        try:
            logging.info(f"Exporting table data as pandas dataframe")
            df:pd.DataFrame  = get_table_as_dataframe(              
                table_name=self.data_ingestion_config.table_name)
            logging.info("Saving Data from Database to local folder ....")           
            raw_data_dir = self.data_ingestion_config.raw_data_dir           
            logging.info(f" Raw Data directory : {raw_data_dir}")
            os.makedirs(raw_data_dir, exist_ok=True)     
            csv_file_name='train.csv'
            raw_file_path = os.path.join(raw_data_dir, csv_file_name)
            df.to_csv(raw_file_path)
            ingest_directory=os.path.join(self.data_ingestion_config.ingested_data_dir)
            os.makedirs(ingest_directory,exist_ok=True)

            ingest_file_path = os.path.join(self.data_ingestion_config.ingested_data_dir, csv_file_name)
            shutil.copy(raw_file_path, ingest_file_path)          
            logging.info(" Data stored in ingested Directory ")
             

            
            return ingest_file_path
            

        except Exception as e:
            raise CustomException(e, sys) from e 
        
        
        
    def split_csv_to_train_test(self,csv_file_path):                   
        train_file_path=self.data_ingestion_config.train_file_path
        test_file_path=self.data_ingestion_config.test_file_path
        
        os.makedirs(train_file_path)
        os.makedirs(test_file_path)
        data = pd.read_csv(csv_file_path,index_col=0)
        size=self.data_ingestion_config.test_size

        
        train_data, test_data = train_test_split(data, test_size=size, random_state=42)

        # Save the training and testing data into separate CSV files
        train_file_path=os.path.join(train_file_path,FILENAME)
        test_file_path=os.path.join(test_file_path,FILENAME)
        
        train_data.to_csv(train_file_path, index=False)
        test_data.to_csv(test_file_path, index=False)
        
        logging.info("---Data Split Done ---")
        logging.info(f"Shape of the data Train Data : {train_data.shape}")
        logging.info(f"Shape of the data Test Data : {test_data.shape}")

        logging.info(f" Train File path : {train_file_path}")
        logging.info(f" Test File path : {test_file_path}")
        
        data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,test_file_path=test_file_path)
        logging.info(f"\n{'>>'*20}Successfully Extracted Data from MySQL Database{'<<'*20} ")
        return data_ingestion_artifact



    def initiate_data_ingestion(self):
        try:
            
            logging.info("Donwloading data from MySQL ")
            ingest_file_path=self.get_data_from_mysql()
            
            logging.info("Splitting data .... ")
            
            return  self.split_csv_to_train_test(csv_file_path=ingest_file_path)

        except Exception as e:
            raise CustomException(e,sys) from e