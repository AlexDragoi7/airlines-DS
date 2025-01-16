import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


gov_airlines = []
countries = []
stakes = []

gov_url = "https://en.wikipedia.org/wiki/List_of_government-owned_airlines"

def gov_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', class_='wikitable')
        rows = table.find_all('tr')

        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                airline_name = columns[0].text.strip()
                country = columns[1].text.strip()
                stake = columns[2].text
                re_stake = re.sub('\[\d+\]', '', stake.strip())
                final_stake = re_stake.replace('[update]', '')
                if final_stake == "":
                    final_stake = "n/a"
                else:
                    final_stake
                gov_airlines.append(airline_name)
                countries.append(country)
                stakes.append(final_stake)
    else:
        print(f"Data could not be retrieved from {gov_url}")

gov_data(gov_url)
gov_df = pd.DataFrame({'Airline': gov_airlines, 'Country': countries, 'Stake': stakes})
print(gov_df)
