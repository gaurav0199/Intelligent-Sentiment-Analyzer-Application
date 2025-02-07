import os,sys
from src.exception import CustomException
from datetime import datetime
from src.utils import read_file
from src.constant import *


config=read_file(CONFIG_FILE_PATH) 
class TrainingPipelineConfig: 
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
            
        except Exception  as e:
            raise CustomException(e,sys)    


class DataIngestionConfig:
    
    def __init__(self,training_pipeline_config):
       
        try:
            data_ingestion_key=config[DATA_INGESTION_CONFIG_KEY] 
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir ,data_ingestion_key[DATA_INGESTION_ARTIFACT_DIR])
            self.raw_data_dir = os.path.join(self.data_ingestion_dir,data_ingestion_key[DATA_INGESTION_RAW_DATA_DIR_KEY])
            self.ingested_data_dir=os.path.join(self.raw_data_dir,data_ingestion_key[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            self.train_file_path = os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_TRAIN_DIR_KEY])
            self.test_file_path = os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_TEST_DIR_KEY])
            self.test_size = 0.2
        except Exception  as e:
            raise CustomException(e,sys)      

