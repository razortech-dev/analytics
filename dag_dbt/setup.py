import setuptools

setuptools.setup(
    name="dag_dbt",
    packages=setuptools.find_packages(exclude=["dag_dbt_tests"]),
    install_requires=[
        "dagster==0.15.5",
        "dagit==0.15.5",
        "pytest",
    ],
)
