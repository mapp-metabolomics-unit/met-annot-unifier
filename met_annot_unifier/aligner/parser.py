from typing import Optional

import pandas as pd


def parse_gnps(file_path: str) -> pd.DataFrame:
    # Read the GNPS output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data


def parse_sirius(file_path: str) -> pd.DataFrame:
    # Read the Sirius output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data


def parse_isdb(file_path: str) -> pd.DataFrame:
    # Read the ISDB output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data


def standardize_column_names(df: pd.DataFrame, original_column_name: str, final_column_name: str) -> pd.DataFrame:
    """
    Standardizes the column names of a dataframe.

    Args:
    df (pandas.DataFrame): The dataframe to standardize.
    original_column_name (str): The current name of the column to be standardized.
    final_column_name (str): The final standardized name for the column.

    Returns:
    pandas.DataFrame: The dataframe with standardized column names.

    Example:
    >>> df = pd.DataFrame({'InChIKey-Planar': [1, 2], 'OtherColumn': [3, 4]})
    >>> standardized_df = standardize_column_names(df, 'InChIKey-Planar', 'InChiKey')
    >>> standardized_df.columns
    Index(['InChiKey', 'OtherColumn'], dtype='object')
    """
    standardized_df = df.rename(columns={original_column_name: final_column_name})
    return standardized_df


def extract_feature_id(df: pd.DataFrame, feature_id_column: str) -> pd.DataFrame:
    """
    Extracts the numeric feature ID from a string in the specified column of a dataframe.

    Args:
    df (pandas.DataFrame): The dataframe containing the feature ID strings.
    feature_id_column (str): The name of the column containing the feature ID strings.

    Returns:
    pandas.DataFrame: The dataframe with the feature ID extracted.

    Example:
    >>> df = pd.DataFrame({'FeatureID': ['573_mapp_batch_00020_gf_sirius_58', '574_mapp_batch_00021_gf_sirius_59']})
    >>> cleaned_df = extract_feature_id(df, 'FeatureID')
    >>> cleaned_df['FeatureID']
    0    58
    1    59
    Name: FeatureID, dtype: int64
    """

    def extract_id(feature_string: Optional[str]) -> Optional[int]:
        if isinstance(feature_string, str):
            # Split the string by '_' and extract the last part, then convert to integer
            return int(feature_string.split("_")[-1])
        else:
            # Handle non-string inputs (like None or NaN)
            # You can decide how to handle this - raise an error, return None, or something else
            return None  # or raise ValueError("Invalid feature string")

    df[feature_id_column] = df[feature_id_column].apply(extract_id)
    return df


def prefix_columns(df: pd.DataFrame, prefix: str, exclude_columns: Optional[list] = None) -> pd.DataFrame:
    """
    Prefixes all columns in a dataframe with the specified prefix, excluding specified columns.

    Args:
    df (pandas.DataFrame): The dataframe to modify.
    prefix (str): The prefix to add to the column names.
    exclude_columns (list, optional): List of column names to exclude from prefixing. Defaults to None.

    Returns:
    pandas.DataFrame: The dataframe with prefixed column names.

    Example:
    >>> df = pd.DataFrame({'feature_id': [1, 2], 'data': [3, 4], 'info': [5, 6]})
    >>> prefixed_df = prefix_columns(df, 'gnps_', exclude_columns=['feature_id'])
    >>> prefixed_df.columns
    Index(['feature_id', 'gnps_data', 'gnps_info'], dtype='object')
    """
    if exclude_columns is None:
        exclude_columns = []

    for column in df.columns:
        if column not in exclude_columns:
            df = df.rename(columns={column: f"{prefix}{column}"})
    return df


def add_source_column(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Adds a 'Source' column to a dataframe, labeling all rows with the specified source name.

    Args:
    df (pandas.DataFrame): The dataframe to modify.
    source_name (str): The name of the source to add (e.g., 'GNPS', 'ISDB', 'SIRIUS').

    Returns:
    pandas.DataFrame: The dataframe with the 'Source' column added.
    """
    df["Source"] = source_name
    return df
