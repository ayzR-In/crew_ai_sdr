import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def llm_outptu_updater(first_name, last_name, title, email, company, llm_output_1):
    connection = None
    try:
        connection = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        dbname = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        port = os.getenv('DB_PORT')
    )
        with connection.cursor() as cur:
            cur.execute('''
                INSERT INTO llm_output(
                        first_name, last_name, title, email, company, llm_output_1
                    ) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT(email) DO NOTHING
                ''' ,(first_name, last_name, title, email, company, llm_output_1))
            connection.commit()
            
    except Exception as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
