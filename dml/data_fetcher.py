import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def llm_data():
    connection = None
    try:
        connection = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        dbname = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        port = os.getenv('DB_PORT')
    )
        with connection.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM llm_data_upstream LIMIT 5")
            row = cur.fetchone()
            return row
    except Exception as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
