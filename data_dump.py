import sys
import pandas as pd
from src.utils import connect_to_mysql
from src.logger import logging
from src.exception import CustomException
table_name = "sentiment_data"


df = pd.read_csv(r'P:\projects\Intelligent-Sentiment-Analyzer-Application\Data\train.csv',index_col=0)

def data_dumping(df,table):
    try:
        conn = connect_to_mysql()
        cursor = conn.cursor()
        query = f"""
            CREATE TABLE IF NOT EXISTS {table} (
            review_text TEXT,
            sentiment VARCHAR(10)
            );"""
    
        logging.info(f"{'>>'*20} Table created......{'<<'*20} \n\n")
        cursor.execute(query)
        insert_query = f"INSERT INTO {table} (review_text, sentiment) VALUES (%s, %s)"
        data_tuples = [tuple(row) for row in df.to_numpy()]
        cursor.executemany(insert_query, data_tuples)

        conn.commit()
        logging.info(f"{'>>'*20} Data dumping completed......{'<<'*20}")
    
        cursor.close()
        conn.close()
    except Exception as e:
        raise CustomException(e,sys) from e
    
if __name__ == '__main__':
    data_dumping(df,table_name)