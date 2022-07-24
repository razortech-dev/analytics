import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from pandas import DataFrame
from dagster import op, Out, In
import logging
from dag_dbt.db_conn import get_postgres_conn

load_dotenv()
filepath1 = os.getenv("CSV1")
filepath2 = os.getenv("CSV2")
tablename1 = os.getenv("TABLE1")
tablename2 = os.getenv("TABLE2")


@op(out={"value1": Out(is_required=True), "value2": Out(is_required=True)})
def get_csv_path(context):
    context.log.info(filepath1)
    context.log.info(filepath2)

    return filepath1, filepath2


@op(out={"table1": Out(is_required=True), "table2": Out(is_required=True)})
def get_tablename(context):
    context.log.info(tablename1)
    context.log.info(tablename2)

    return tablename1, tablename2


@op(ins={"filepath": In(str)}, out={"df": Out(is_required=True)})
def fetch_data_v2(context, filepath):
    try:
        lgr = logging.getLogger('console_logger')

        df = pd.read_csv(filepath, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
        context.log.info(df.head())
        lgr.error(df)
        return df

    except Exception as e:
        print("Data extract error: " + str(e))


@op(ins={"df": In(DataFrame), "tablename": In(str)})
def ingest_data_to_postgres_v2(context, df: DataFrame, tablename):
    try:
        lgr = logging.getLogger("console_logger")
        context.log.info(tablename)
        context.log.info(df.head())
        lgr.error(df.head())

        engine = get_postgres_conn()
        context.log.info(engine)

        df.to_sql(tablename, engine, if_exists='replace', index=False, schema="public")
        context.log.info("Data ingestion successful")
    except Exception as e:
        print("Data load error: " + str(e))
        lgr.error(str(e))
