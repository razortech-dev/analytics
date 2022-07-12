import numpy as np
import pandas as pd
from pandas import DataFrame
from dagster import op, Out, Output
import logging
from dag_dbt.db_conn import get_postgres_conn


@op(out={"df": Out(is_required=True)})
def fetch_data(context):
    try:
        lgr = logging.getLogger('console_logger')

        filepath = '/home/razortech/Downloads/datasets/NH_ProviderInfo_Jun2022.csv'
        df = pd.read_csv(filepath, sep=',', encoding='cp1252').replace(to_replace='null', value=np.NaN)
        context.log.info(df.head())
        lgr.error(df)
        yield Output(df, "df")

    except Exception as e:
        print("Data extract error: " + str(e))


# load data to postgres
@op
def ingest_data_to_postgres(context, df: DataFrame):
    try:
        lgr = logging.getLogger("console_logger")
        # print info and errors
        context.log.info(df.head())
        lgr.error(df.head())
        # save df to postgres
        engine = get_postgres_conn()
        df.to_sql(f'stg_testdata', engine, if_exists='replace', index=False, schema="public")
        # print success message
        context.log.info("Data ingestion successful")
    except Exception as e:
        print("Data load error: " + str(e))
        lgr.error(str(e))
