from dagster import job

from dag_dbt.ops.ingest import ingest_data_to_postgres, fetch_data


@job
def run_ingest_job():

    df = fetch_data()
    ingest_data_to_postgres(df)
