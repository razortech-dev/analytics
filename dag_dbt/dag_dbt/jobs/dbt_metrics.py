from dagster_dbt import dbt_cli_resource
from dag_dbt.ops.dbt import dag_dbt_run, dag_dbt_test
from dag_dbt.resources import RESOURCES_LOCAL
# from dag_dbt.resources.dbt_asset_resource import PostgresDbtAssetResource
# from dag_dbt.resources.postgres_io_manager import POSTGRES_CONFIG

from dagster import ResourceDefinition, graph
from dagster.utils import file_relative_path

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dag_dbt_data")
DBT_PROFILES_DIR = DBT_PROJECT_DIR + "/config"
dbt_local_resource = dbt_cli_resource.configured(
    {"profiles-dir": DBT_PROFILES_DIR, "project-dir": DBT_PROJECT_DIR, "target": "local"}
)


@graph
def dbt_metrics():
    dag_dbt_test(dag_dbt_run())


dbt_local_job = dbt_metrics.to_job(
    resource_defs={
        **RESOURCES_LOCAL,
        **{
            "dbt": dbt_local_resource,
            # "dbt_assets": ResourceDefinition.hardcoded_resource(
            #     PostgresDbtAssetResource(
            #         {**{"database": "testdata"}, **POSTGRES_CONFIG}, "stg_testdata"
            #     )
            # ),
            # "partition_bounds": ResourceDefinition.none_resource(),
        },
    }
)
