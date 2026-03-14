import pandas as pd

def load_data():

    url = "https://raw.githubusercontent.com/yourname/egsa-data/main/awo2025.csv"

    df = pd.read_csv(url)

    return df