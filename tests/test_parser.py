from met_annot_unifier.aligner.parser import parse_gnps, parse_isdb, parse_sirius

# Path to your sample data files
GNPS_SAMPLE_PATH = "tests/data/gnps_output_example.tsv"
SIRIUS_SAMPLE_PATH = "tests/data/sirius_output_example.tsv"
ISDB_SAMPLE_PATH = "tests/data/isdb_output_example.tsv"


def test_parse_gnps():
    # Load the sample GNPS data
    gnps_data = parse_gnps(GNPS_SAMPLE_PATH)

    # Assertions to check if the data is loaded correctly
    assert not gnps_data.empty, "Dataframe is empty"
    assert "#Scan#" in gnps_data.columns, "feature_id column is missing"
    assert "InChIKey-Planar" in gnps_data.columns, "IK2D column is missing"
    # ... add more assertions as needed ...


def test_parse_sirius():
    # Load the sample Sirius data
    sirius_data = parse_sirius(SIRIUS_SAMPLE_PATH)

    # Similar assertions for Sirius data
    assert not sirius_data.empty, "Dataframe is empty"
    assert "id" in sirius_data.columns, "feature_id column is missing"
    assert "InChIkey2D" in sirius_data.columns, "IK2D column is missing"
    # ... add more assertions as needed ...


def test_parse_isdb():
    # Load the sample ISDB data
    isdb_data = parse_isdb(ISDB_SAMPLE_PATH)

    # Similar assertions for ISDB data
    assert not isdb_data.empty, "Dataframe is empty"
    assert "feature_id" in isdb_data.columns, "feature_id column is missing"
    assert "short_inchikey" in isdb_data.columns, "IK2D column is missing"
    # ... add more assertions as needed ...
