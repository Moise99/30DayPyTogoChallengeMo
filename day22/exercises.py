#1. Scrape the following website and store the data as json file(url ='http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json
def scrape_bu_facts():
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    facts = {}
    for item in soup.select('.facts-list li'):
        strong_tag = item.find('strong')
        if strong_tag is not None:
            key = strong_tag.get_text(strip=True)
            value = item.get_text(strip=True).replace(key, '').strip()
            facts[key] = value
    with open('bu_facts.json', 'w') as f:
        json.dump(facts, f, indent=4)
# Call the function to execute the scraping
scrape_bu_facts()

# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
import requests
from bs4 import BeautifulSoup
import json
def scrape_uci_datasets():
    url = 'https://archive.ics.uci.edu/datasets.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'border': '1'})
    datasets = []
    if table is not None:
        for row in table.find_all('tr')[1:]:  # Skip header row
            cols = row.find_all('td')
            if len(cols) >= 2:
                dataset = {
                    'name': cols[0].get_text(strip=True),
                    'description': cols[1].get_text(strip=True),
                    'link': cols[0].find('a')['href'] if cols[0].find('a') else None
                }
                datasets.append(dataset)
    else:
        print("Table not found on the page.")
    with open('uci_datasets.json', 'w') as f:
        json.dump(datasets, f, indent=4)
# Call the function to execute the scraping
scrape_uci_datasets()

#3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
import requests
from bs4 import BeautifulSoup
import json
def scrape_us_presidents():
    url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    presidents = []
    if table is not None:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')   
            if len(cols) >= 3:
                president = {
                    'number': cols[0].get_text(strip=True),
                    'name': cols[1].get_text(strip=True),
                    'term_start': cols[2].get_text(strip=True),
                    'term_end': cols[3].get_text(strip=True) if len(cols) > 3 else None,
                    'party': cols[4].get_text(strip=True) if len(cols) > 4 else None
                }
                presidents.append(president)
    else:
        print("Table not found on the page.")
    with open('us_presidents.json', 'w') as f:
        json.dump(presidents, f, indent=4)
# Call the function to execute the scraping
scrape_us_presidents()