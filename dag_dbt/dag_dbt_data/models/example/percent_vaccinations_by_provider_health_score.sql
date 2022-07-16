{{ config(materialized='table') }}

with source_data as (

    select "NH_ProviderInfo_Jun2022_data"."Federal Provider Number",
           "Provider Name",
           "Total Weighted Health Survey Score",
           "Percent Vaccinated Residents"
    from "NH_ProviderInfo_Jun2022_data"
    join "NH_CovidVaxProvider_20220626_data"
    on "NH_ProviderInfo_Jun2022_data"."Federal Provider Number"
           = "NH_CovidVaxProvider_20220626_data"."Federal Provider Number"

)

select *
from source_data
