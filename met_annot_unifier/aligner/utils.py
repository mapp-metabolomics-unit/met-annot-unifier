# Function to determine matching sources
import json
from importlib import resources
from typing import Any, Dict, cast

import pandas as pd


def determine_source(row: pd.Series) -> str:
    sources = []
    # Check if all are equal
    if row["gnps_IK2D"] == row["sirius_IK2D"] == row["isdb_IK2D"]:
        return "GNPS,ISDB,SIRIUS"
    if row["gnps_IK2D"] == row["sirius_IK2D"]:
        sources.append("GNPS")
        sources.append("SIRIUS")
    if row["gnps_IK2D"] == row["isdb_IK2D"]:
        sources.append("GNPS")
        sources.append("ISDB")
    if row["sirius_IK2D"] == row["isdb_IK2D"]:
        sources.append("ISDB")
        sources.append("SIRIUS")
    return "|".join(sorted(set(sources)))


# Function to count the sources
def count_sources(source_str: str) -> int:
    if source_str:
        # Count unique source names (they are | separated)
        return len(set(source_str.split("|")))
    return 0


def table_pruner(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Function to remove columns from a DataFrame
    Args:
    df (pandas.DataFrame): Input DataFrame
    columns (list): List of columns to remove

    Returns:
    pandas.DataFrame: DataFrame with specified columns removed
    """
    return df.drop(columns=columns, axis=1)


def load_configuration(config_filename: str) -> Dict[str, Any]:
    """
    Function to load configuration from a JSON file.

    Args:
        config_filename (str): Filename of the configuration file to load.

    Returns:
        Dict[str, Any]: Configuration dictionary.
    """
    with resources.open_text("met_annot_unifier.config", config_filename) as config_file:
        config = json.load(config_file)

    # Cast the loaded config to Dict[str, Any] to satisfy type checkers
    return cast(Dict[str, Any], config)
