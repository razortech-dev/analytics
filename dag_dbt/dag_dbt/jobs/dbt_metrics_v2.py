from dag_dbt.ops.dbt import dag_dbt_run, dag_dbt_test
# from dag_dbt.ops.ingest_v2 import get_csv_path, get_tablename, fetch_data_v2, ingest_data_to_postgres_v2
from dag_dbt.ops.ingest_v3 import load_data
from dag_dbt.resources import RESOURCES_LOCAL
from dagster import graph
from dagster.utils import file_relative_path
from dagster_dbt import dbt_cli_resource

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dag_dbt_data")
DBT_PROFILES_DIR = DBT_PROJECT_DIR + "/config"
dbt_local_resource = dbt_cli_resource.configured(
    {"profiles-dir": DBT_PROFILES_DIR, "project-dir": DBT_PROJECT_DIR, "target": "local"}
)


@graph
def dbt_metrics_v2():
    # path1, path2 = get_csv_path()
    # tablename1, tablename2 = get_tablename()
    #
    # df1 = fetch_data_v2.alias("csv1_data")(path1)
    # df2 = fetch_data_v2.alias("csv2_data")(path2)
    # loaded1 = ingest_data_to_postgres_v2.alias("ingest_file_1")(df1, tablename1)
    # loaded2 = ingest_data_to_postgres_v2.alias("ingest_file_2")(df2, tablename2)
    #
    # dag_dbt_test(dag_dbt_run(source1=loaded1, source2=loaded2))

    load = load_data()
    dag_dbt_test(dag_dbt_run(source=load))


dbt_local_job_v2 = dbt_metrics_v2.to_job(
    resource_defs={
        **RESOURCES_LOCAL,
        **{"dbt": dbt_local_resource},
    }
)
