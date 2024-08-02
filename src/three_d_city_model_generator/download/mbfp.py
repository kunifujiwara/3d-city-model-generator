#To download microsoft building footprints

import pandas as pd

from utils import download_file

def get_geojson_links():
    
    # URL of the file you want to download
    url = "https://minedbuildings.blob.core.windows.net/global-buildings/dataset-links.csv"

    # Local filename to save the downloaded file
    filename = "dataset-links.csv"

    # Call the function to download the file
    download_file(url, filename)

    data_types = {
        'Location': 'str',
        'QuadKey': 'str',
        'Url': 'str',
        'Size': 'str'
    }

    df_links = pd.read_csv("dataset-links.csv", dtype=data_types)
    
    return df_links