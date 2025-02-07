import os
from src.pipeline.training_pipeline.data_ingestion_pipe import data_ingestion

#Hi, nice to see you!😊
#For complete project or any collaboration contact me
#
if __name__ == '__main__':

    file_path = 'params.yaml'
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    else:
        print(f"The file {file_path} does not exist.")

    data_ingestion()
