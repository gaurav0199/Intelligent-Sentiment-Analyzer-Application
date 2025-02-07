from src.exception import CustomException
from src.utils import write_file
from src.entity.config_entity import *
from src.entity.artifact_entity import *
from src.components.data_ingestion import DataIngestion
import  sys




class data_ingestion():

    def __init__(self,training_pipeline_config) -> None:
        try:
            
            self.training_pipeline_config=training_pipeline_config
            data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(self.training_pipeline_config))
            
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            
            data_ingestion_artifact_report={ 'data_ingestion_artifact' :{
                                            'train_file_path': data_ingestion_artifact.train_file_path,
                                              'test_file_path' : data_ingestion_artifact.test_file_path
                                            }}
            
            write_file(data=data_ingestion_artifact_report)
        
            
        except Exception as e:
            raise CustomException(e, sys) from e

        
