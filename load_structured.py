import pandas as pd
import os


def load_data():
    # This gets the absolute path to the 'EndometriosisResearch' folder
    # by going up one level from the 'src' folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "structured_endometriosis_data.csv")
    # clinical_clusters_output.csv
    # structured_endometriosis_data.csv
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    else:
        print(f"File not found at: {data_path}")
        return None
