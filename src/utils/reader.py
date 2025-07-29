def load_yaml(yaml_path):
    import yaml
    with open(yaml_path, "r") as file:
        config_dict = yaml.safe_load(file)
    return config_dict

def load_json(json_path):
    import json
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def load_csv(csv_path: str):
    import pandas as pd
    return pd.read_csv(csv_path)

def load_csv_polars(csv_path: str):
    import polars as pl
    """
    Loads a CSV file into a Polars DataFrame.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pl.DataFrame: Loaded Polars DataFrame.
    """
    return pl.read_csv(csv_path)