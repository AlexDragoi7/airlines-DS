import gov_airlines_scrape as gov_airlines
# import pandas as pd


gov_airlines_csv = 'gov_airlines.csv'

def load_to_csv(df, csv_file):
    return df.to_csv(csv_file)

load_to_csv(gov_airlines.gov_df, gov_airlines_csv)