import os
from dagster_dbt import load_assets_from_dbt_project
from dagster_dbt import dbt_cli_resource
from dagster import (
    file_relative_path,
    define_asset_job,
    AssetSelection,
    ScheduleDefinition
)

resources = {

        "dbt": dbt_cli_resource.configured(
            {"project_dir": os.getenv("DBT_PROJECT_DIR"), "profiles_dir": os.getenv("DBT_PROFILES_DIR")}
        )
    }

dbt_assets = load_assets_from_dbt_project(os.getenv("DBT_PROJECT_DIR"), os, key_prefix = ["dbt_assets"])
