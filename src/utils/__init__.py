import os
import yaml
from src.logger import logging
import pymysql
from dotenv import load_dotenv

import pandas as pd
from src.logger import logging
from src.exception import CustomException

import os,sys
import yaml
import dill


env_file_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_file_path)



def connect_to_mysql():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        logging.info("Successfully connected to MySQL database.")
        return connection
    except Exception as e:
            raise CustomException(e,sys) from e
def get_table_as_dataframe(table_name:str)->pd.DataFrame:
    
    connection = connect_to_mysql()
    if not connection:
            return None
    try:  
        logging.info(f"Reading data from database: {DB_NAME} and table: {table_name}")
        query = f"SELECT * FROM {table_name}"            
        df = pd.read_sql(query, connection)
        connection.close()
        logging.info(f"Successfully fetched {df.shape[0]} rows from {table_name}.")
        return df
    except Exception as e:
        raise CustomException(e,sys) from e


def read_file(file_path:str)->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys) from e
    
def write_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise CustomException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok= True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys) from e










