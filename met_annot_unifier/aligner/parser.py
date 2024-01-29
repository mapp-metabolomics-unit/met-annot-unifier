import pandas as pd


def parse_gnps(file_path):
    # Read the GNPS output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data


def parse_sirius(file_path):
    # Read the Sirius output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data


def parse_isdb(file_path):
    # Read the ISDB output file
    data = pd.read_csv(file_path, sep="\t")
    # Extract necessary columns and any other processing
    return data
