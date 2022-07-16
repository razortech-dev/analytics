from dagster_dbt import DbtCliOutput

from dagster import Out, Output, op


@op(
    required_resource_keys={"dbt"},
    out=Out(dagster_type=DbtCliOutput),
    tags={"kind": "dbt"},
)
def dag_dbt_run(context):
    dbt_cli_output = context.resources.dbt.run()

    # for materialization in context.resources.dbt_assets.get_asset_materializations(dbt_cli_output):
    #     yield materialization
    yield Output(dbt_cli_output)


@op(required_resource_keys={"dbt"}, tags={"kind": "dbt"})
def dag_dbt_test(context, _dbt_output):
    context.resources.dbt.test()
