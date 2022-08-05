import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def get_postgres_conn(db_host):
    # load_dotenv()
    # pwd = os.getenv("DB_PASSWORD")
    # uid = os.getenv("DB_USERNAME")
    # db = os.getenv("DB_NAME")

    pwd = "mypass"
    uid = "myuser"
    db = "demodb"

    server = db_host
    port = 5432

    cs = create_engine(f'postgresql+psycopg2://{uid}:{pwd}@{server}:{port}/{db}')

    try:
        return cs
    except Exception as e:
        print("Error loading the config file." + str(e))
