from dagster import repository

from dag_dbt.jobs.say_hello import say_hello_job
from dag_dbt.schedules.my_hourly_schedule import my_hourly_schedule
from dag_dbt.sensors.my_sensor import my_sensor
from dag_dbt.jobs.run_ingest import run_ingest_job

from dag_dbt.jobs.dbt_metrics import dbt_local_job


@repository
def dag_dbt():
    """
    The repository definition for this dag_dbt Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job, run_ingest_job, dbt_local_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
