import os

FILENAME='data.csv'
CONFIG_DIR='config'
SCHEMA_FILE='config.yaml'
CONFIG_FILE_PATH=os.path.join(os.getcwd(),CONFIG_DIR,SCHEMA_FILE)
CONFIG_DIR='config'
SCHEMA_FILE='schema.yaml'
SCHEMA_FILE_PATH=os.path.join(os.getcwd(),CONFIG_DIR,SCHEMA_FILE)



DATA_INGESTION_DATABASE_NAME= "data_base"
DATA_INGESTION_TABLE_NAME= "table_name"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"
CONFIG_FILE_KEY = "config"

