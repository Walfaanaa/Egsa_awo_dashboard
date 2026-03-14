import pandas as pd

def load_data():

    url = "https://raw.githubusercontent.com/Walfaanaa/Egsa_awo_dashboard/main/AWO.csv"

    df = pd.read_csv(url)

    return df
