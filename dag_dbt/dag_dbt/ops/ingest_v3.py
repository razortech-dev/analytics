import logging

import pandas as pd
import numpy as np

import os
import glob
from dotenv import load_dotenv
from dagster import op, configured
from dag_dbt.db_conn import get_postgres_conn


load_dotenv()
# data_dir = os.getenv("DATA_DIR")


@op(config_schema={"data_dir": str, "db_host": str})
def load_data(context):
    try:
        data_dir = context.op_config["data_dir"]
        context.log.info(data_dir)

        lgr = logging.getLogger('console_logger')
        context.log.info(os.getcwd())

        csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
        count = 1

        for f in csv_files:
            df = pd.read_csv(f, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
            context.log.info(df.head())
            lgr.error(df.head())

            db_host = context.op_config["db_host"]
            engine = get_postgres_conn(db_host)
            context.log.info(engine)

            df.to_sql("model_" + str(count), engine, if_exists='replace', index=False, schema="public")
            count = count + 1
            context.log.info("Data ingestion successful")

    except Exception as e:
        print("Data load error: " + str(e))


DATA_DIR = "/opt/dagster/app/data/"
DB_HOST = "192.168.1.38"
load_data_config = configured(load_data, name="load_data_config")(
    {"data_dir": DATA_DIR,
     "db_host": DB_HOST}
)
