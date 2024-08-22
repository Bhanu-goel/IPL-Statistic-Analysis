import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_table(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Identify the table element
            table = soup.find_all('table',class_='table mc-scorecard__table t-SA')

            for i, table in enumerate(table):
                class_name = table.get('class')
                print(f'Class name of table {i + 1}:', class_name)
            # Use pandas to read the HTML table into a DataFrame
            df = pd.read_html(str(table))[0]

            return df

        else:
            print('Failed to retrieve the web page. Status code:', response.status_code)
            return None

    except Exception as e:
        print('An error occurred:', e)
        return None

# URL of the webpage with the table
url = 'https://www.cricketworldcup.com/match/102782'

# Call the function to scrape the table


scrap_interval = 1
while True:
    table_data = scrape_table(url)

    if table_data is not None:
        # Print the DataFrame
        print(table_data)
        print()
    time.sleep(scrap_interval)
