{{ config(materialized='table') }}

with source_data as (

    select "NH_ProviderInfo_Jun2022"."Federal Provider Number",
           "Provider Name",
           "Total Weighted Health Survey Score",
           "Percent Vaccinated Residents"
    from "NH_ProviderInfo_Jun2022"
    join "NH_CovidVaxProvider_20220626"
    on "NH_ProviderInfo_Jun2022"."Federal Provider Number"
           = "NH_CovidVaxProvider_20220626"."Federal Provider Number"

)

select *
from source_data
