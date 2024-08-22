import requests
from bs4 import BeautifulSoup

def scrapwebsite(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            tables = soup.find_all('table')
            return tables
        else:
            print('Failed to retrieve the web page. Status code:', response.status_code)
            return None
    except Exception as e:
        print('An error occurred:', e)
        return None

# URL of the webpage with the table
url = 'https://www.cricketworldcup.com/match/102782'
table_data = scrapwebsite(url)
for t in table_data:
    print(t)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
