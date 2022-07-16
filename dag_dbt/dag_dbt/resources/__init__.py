from dagstermill.io_managers import local_output_notebook_io_manager

# from dag_dbt.resources.postgres_io_manager import local_postgres_io_manager

RESOURCES_LOCAL = {
    # "postgres_io_manager": local_postgres_io_manager,
    "output_notebook_io_manager": local_output_notebook_io_manager,
}
