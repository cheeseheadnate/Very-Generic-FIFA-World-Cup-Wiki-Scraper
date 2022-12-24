from bs4 import BeautifulSoup
import requests
import pandas as pd

# Based on Wikipedia for educational purposes

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]

def get_matches(year):
   web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
   response = requests.get(web)
   content = response.text
   soup = BeautifulSoup(content, 'lxml')

   matches = soup.find_all('div', class_='footballbox')

   home = []
   score = []
   away = []

   for match in matches:
      home.append(match.find('th', class_='fhome').get_text())
      score.append(match.find('th', class_='fscore').get_text())
      away.append(match.find('th', class_='faway').get_text())

   dict_football = { 'home': home , 'score': score , 'away': away }

   footballDF = pd.DataFrame(dict_football)
   footballDF['year'] = year
   return footballDF


# Historical Data
fifa = [get_matches(year) for year in years]
fifaDF = pd.concat(fifa, ignore_index=True)
fifaDF.to_csv('fifa_worldcup_historical_data.csv', index=False)


# Fixture
fixtureDF = get_matches('1938')
fixtureDF.to_csv('fifa_worldcup_fixture.csv', index=False)

# Output for testing
print(fixtureDF)