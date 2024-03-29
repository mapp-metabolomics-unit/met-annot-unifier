import pandas as pd

from met_annot_unifier.aligner.parser import (
    add_source_column,
    extract_feature_id,
    prefix_columns,
    standardize_column_names,
)


def align_data(gnps_file: str, sirius_file: str, isdb_file: str) -> pd.DataFrame:
    """
    Aligns and merges data from GNPS, Sirius, and ISDB datasets. The function standardizes
    column names, prefixes them to indicate their source, merges the data based on 'feature_id'
    and 'IK2D', and then creates consolidated 'Sources' and 'SMILES' columns.

    Args:
    gnps_file (str): File path for the GNPS data in TSV format.
    sirius_file (str): File path for the Sirius data in TSV format.
    isdb_file (str): File path for the ISDB data in TSV format.

    Returns:
    pandas.DataFrame: A DataFrame with aligned and merged data from GNPS, Sirius, and ISDB.

    Example:
    >>> gnps_file = 'path/to/gnps_data.tsv'
    >>> sirius_file = 'path/to/sirius_data.tsv'
    >>> isdb_file = 'path/to/isdb_data.tsv'
    >>> aligned_data = align_data(gnps_file, sirius_file, isdb_file)
    >>> print(aligned_data.columns)
    Index(['feature_id', 'IK2D', 'Sources', 'SMILES', ...], dtype='object')
    """

    # Read and process GNPS data
    gnps_data = pd.read_csv(gnps_file, sep="\t")
    gnps_data = add_source_column(gnps_data, "GNPS")
    gnps_data = standardize_column_names(gnps_data, "InChIKey-Planar", "IK2D")
    gnps_data = standardize_column_names(gnps_data, "#Scan#", "feature_id")
    gnps_data = standardize_column_names(gnps_data, "Smiles", "SMILES")
    gnps_data = prefix_columns(gnps_data, "gnps_", exclude_columns=[])
    gnps_data = standardize_column_names(gnps_data, "gnps_IK2D", "IK2D")
    gnps_data = standardize_column_names(gnps_data, "gnps_feature_id", "feature_id")

    # For debugging we pprint the dataframes
    # pprint(gnps_data)

    # Read and process Sirius data
    sirius_data = pd.read_csv(sirius_file, sep="\t")
    sirius_data = add_source_column(sirius_data, "SIRIUS")
    sirius_data = standardize_column_names(sirius_data, "InChIkey2D", "IK2D")
    sirius_data = standardize_column_names(sirius_data, "id", "feature_id")
    sirius_data = standardize_column_names(sirius_data, "smiles", "SMILES")
    sirius_data = prefix_columns(sirius_data, "sirius_", exclude_columns=[])
    sirius_data = extract_feature_id(sirius_data, "sirius_feature_id")
    sirius_data = standardize_column_names(sirius_data, "sirius_IK2D", "IK2D")
    sirius_data = standardize_column_names(sirius_data, "sirius_feature_id", "feature_id")

    # For debugging we pprint the dataframes
    # pprint(sirius_data)

    # Read and process ISDB data
    isdb_data = pd.read_csv(isdb_file, sep="\t")
    isdb_data = add_source_column(isdb_data, "ISDB")
    isdb_data = standardize_column_names(isdb_data, "short_inchikey", "IK2D")
    isdb_data = standardize_column_names(isdb_data, "feature_id", "feature_id")
    isdb_data = standardize_column_names(isdb_data, "structure_smiles", "SMILES")
    isdb_data = prefix_columns(isdb_data, "isdb_", exclude_columns=[])
    isdb_data = standardize_column_names(isdb_data, "isdb_IK2D", "IK2D")
    isdb_data = standardize_column_names(isdb_data, "isdb_feature_id", "feature_id")

    # For debugging we pprint the dataframes
    # pprint(isdb_data)

    # Merge the dataframes on 'feature_id' and 'InChiKey' with an outer join
    combined_data = pd.concat([gnps_data, sirius_data, isdb_data], axis=0, ignore_index=True)
    # Group by 'feature_id' and 'IK2D' and combine the annotations
    merged_data = combined_data.groupby(["feature_id", "IK2D"], as_index=False).agg(
        lambda x: ", ".join(x.dropna().astype(str).unique())
    )

    # Create the 'Sources' column by concatenating sirius_Source, isdb_Source, and gnps_Source
    merged_data["Sources"] = merged_data.apply(
        lambda row: ", ".join(filter(None, [row.get("sirius_Source"), row.get("isdb_Source"), row.get("gnps_Source")])),
        axis=1,
    )

    # Create a SMILES column by choosing form the sirius_SMILES, isdb_SMILES, and gnps_smiles columns with this order of preference (sirius, isdb, gnps)

    merged_data["SMILES"] = merged_data.apply(
        lambda row: row.get("sirius_SMILES")
        if row.get("sirius_SMILES")
        else row.get("isdb_SMILES")
        if row.get("isdb_SMILES")
        else row.get("gnps_SMILES"),
        axis=1,
    )

    # Select columns

    selected_columns = ["feature_id", "IK2D", "Sources", "SMILES"]

    # Place the selected columns at the front of the dataframe

    merged_data = merged_data[
        selected_columns + [column for column in merged_data.columns if column not in selected_columns]
    ]

    return merged_data
