import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def get_postgres_conn():
    load_dotenv()
    pwd = os.getenv("DB_PASSWORD")
    uid = os.getenv("DB_USERNAME")
    server = os.getenv("DB_SERVER")
    db = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT")

    cs = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')

    try:
        return cs
    except:
        print("Error loading the config file.")
