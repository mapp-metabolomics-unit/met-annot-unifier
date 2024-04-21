import os
import tempfile

import pandas as pd

from met_annot_unifier.aligner.aligner import align_data_horizontally, align_data_vertically


def test_align_data_vertically():
    # Mock data for GNPS, Sirius, and ISDB
    gnps_mock = pd.DataFrame({"#Scan#": [1, 2], "InChIKey-Planar": ["IK1", "IK2"], "Smiles": ["smile1", "smile2"]})
    sirius_mock = pd.DataFrame(
        {"id": ["546_test_1", "546_test_3"], "InChIkey2D": ["IK1", "IK3"], "smiles": ["smile1", "smile3"]}
    )
    isdb_mock = pd.DataFrame(
        {"feature_id": [2, 3], "short_inchikey": ["IK2", "IK3"], "structure_smiles": ["smile2", "smile3"]}
    )

    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_gnps, tempfile.NamedTemporaryFile(
        delete=False, suffix=".tsv", mode="w"
    ) as tf_sirius, tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_isdb:
        gnps_mock.to_csv(tf_gnps.name, sep="\t", index=False)
        # pprint(gnps_mock)
        sirius_mock.to_csv(tf_sirius.name, sep="\t", index=False)
        # pprint(sirius_mock)
        isdb_mock.to_csv(tf_isdb.name, sep="\t", index=False)
        # pprint(isdb_mock)

        # Call the align_data function
        merged_data = align_data_vertically(tf_gnps.name, tf_sirius.name, tf_isdb.name)

    # Assertions
    assert "feature_id" in merged_data.columns
    assert "IK2D" in merged_data.columns
    assert "Sources" in merged_data.columns
    assert "SMILES" in merged_data.columns
    assert len(merged_data) == 3  # Expecting 3 merged rows

    # Check if 'Sources' column is correctly populated
    for source in ["GNPS|SIRIUS", "GNPS|ISDB", "ISDB|SIRIUS"]:
        assert source in merged_data["Sources"].values

    # Clean up: Remove temporary files
    os.remove(tf_gnps.name)
    os.remove(tf_sirius.name)
    os.remove(tf_isdb.name)


def test_align_data_vertically_partial():
    # Mock data for GNPS, Sirius, and ISDB
    gnps_mock = pd.DataFrame({"#Scan#": [1, 2], "InChIKey-Planar": ["IK1", "IK2"], "Smiles": ["smile1", "smile2"]})
    sirius_mock = pd.DataFrame(
        {"id": ["546_test_1", "546_test_3"], "InChIkey2D": ["IK1", "IK3"], "smiles": ["smile1", "smile3"]}
    )
    isdb_mock = pd.DataFrame(
        {"feature_id": [2, 3], "short_inchikey": ["IK2", "IK3"], "structure_smiles": ["smile2", "smile3"]}
    )

    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_gnps, tempfile.NamedTemporaryFile(
        delete=False, suffix=".tsv", mode="w"
    ) as tf_sirius, tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_isdb:
        gnps_mock.to_csv(tf_gnps.name, sep="\t", index=False)
        # pprint(gnps_mock)
        sirius_mock.to_csv(tf_sirius.name, sep="\t", index=False)
        # pprint(sirius_mock)
        isdb_mock.to_csv(tf_isdb.name, sep="\t", index=False)
        # pprint(isdb_mock)

        # Call the align_data function
        merged_data = align_data_vertically(gnps_file=tf_gnps.name, isdb_file=tf_isdb.name)

    # Assertions
    assert "feature_id" in merged_data.columns
    assert "IK2D" in merged_data.columns
    assert "Sources" in merged_data.columns
    assert "SMILES" in merged_data.columns
    assert len(merged_data) == 3  # Expecting 3 merged rows

    # Check if 'Sources' column is correctly populated
    for source in ["GNPS", "GNPS|ISDB", "ISDB"]:
        assert source in merged_data["Sources"].values

    # Clean up: Remove temporary files
    os.remove(tf_gnps.name)
    os.remove(tf_sirius.name)
    os.remove(tf_isdb.name)


def test_align_data_horizontally():
    # Mock data for GNPS, Sirius, and ISDB
    gnps_mock = pd.DataFrame(
        {"#Scan#": [1, 2, 4], "InChIKey-Planar": ["IK1", "IK2", ""], "Smiles": ["smile1", "smile2", ""]}
    )
    sirius_mock = pd.DataFrame(
        {"id": ["546_test_1", "546_test_3"], "InChIkey2D": ["IK1", "IK3"], "smiles": ["smile1", "smile3"]}
    )
    isdb_mock = pd.DataFrame(
        {"feature_id": [2, 3], "short_inchikey": ["IK2", "IK3"], "structure_smiles": ["smile2", "smile3"]}
    )

    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_gnps, tempfile.NamedTemporaryFile(
        delete=False, suffix=".tsv", mode="w"
    ) as tf_sirius, tempfile.NamedTemporaryFile(delete=False, suffix=".tsv", mode="w") as tf_isdb:
        gnps_mock.to_csv(tf_gnps.name, sep="\t", index=False)
        # pprint(gnps_mock)
        sirius_mock.to_csv(tf_sirius.name, sep="\t", index=False)
        # pprint(sirius_mock)
        isdb_mock.to_csv(tf_isdb.name, sep="\t", index=False)
        # pprint(isdb_mock)

        # Call the align_data function
        merged_data = align_data_horizontally(tf_gnps.name, tf_sirius.name, tf_isdb.name)

    # Assertions

    print(merged_data.columns)
    print(merged_data)
    assert "feature_id" in merged_data.columns
    assert "IK2D" not in merged_data.columns
    assert "source" in merged_data.columns
    assert "source_number" in merged_data.columns
    assert "sirius_Source" not in merged_data.columns
    assert len(merged_data) == 4  # Expecting 3 merged rows

    # Check if 'Sources' column is correctly populated
    for source in ["GNPS|SIRIUS", "GNPS|ISDB", "ISDB|SIRIUS", ""]:
        assert source in merged_data["source"].values

    # Clean up: Remove temporary files
    os.remove(tf_gnps.name)
    os.remove(tf_sirius.name)
    os.remove(tf_isdb.name)
