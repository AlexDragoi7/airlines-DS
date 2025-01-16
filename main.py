import gov_airlines_scrape as gov_airlines
import former_gov_airlines_scrape as former_gov_airlines



gov_airlines_csv = 'gov_airlines.csv'
former_gov_airlines_csv = 'former_gov_airlines.csv'

def load_to_csv(df, csv_file):
    return df.to_csv(csv_file)

# load_to_csv(gov_airlines.gov_df, gov_airlines_csv) -- enable to create a dataset with the current government owned airlines
# load_to_csv(former_gov_airlines.former_gov_df, former_gov_airlines_csv) -- enable to create a dataset with the former government owned airlines