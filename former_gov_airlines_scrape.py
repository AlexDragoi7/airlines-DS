import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


airlines = []
countries = []
end_of_ownership = []
fate = []

data_url = "https://en.wikipedia.org/wiki/List_of_government-owned_airlines"

def former_gov_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = BeautifulSoup(response.text, 'html.parser')
        tables = data.find_all('table', class_='wikitable')
        
        rows = tables[1].find_all('tr')
        for row in rows[1:]:
            column = row.find_all('td')
            if len(column) >= 4:
                airline_name:str = column[0].text.strip()
                country_name:str = column[1].text.strip()
                gov_ownership:int = column[2].contents[0][:-1]
                final_decision:str = column[3].text
                re_final_decision = re.sub('\[\d+\]','',final_decision.strip())

                airlines.append(airline_name)
                countries.append(country_name)
                end_of_ownership.append(gov_ownership)
                fate.append(re_final_decision)

    else:
        print(f"Data could not be retrieved from {data_url}")

former_gov_data(data_url)
former_gov_df = pd.DataFrame({'Airline': airlines, 'Country': countries, 'End of ownership': end_of_ownership, 'Fate': fate})
print(former_gov_df)