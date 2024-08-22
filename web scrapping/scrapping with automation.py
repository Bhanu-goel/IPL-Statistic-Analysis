import requests
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Now you can use BeautifulSoup to extract data from the page
            # For example, let's extract all the links on the page
            links = soup.find_all('a')

            # Print the links
            for link in links:
                print(link.get('href'))

        else:
            print('Failed to retrieve the web page. Status code:', response.status_code)

    except Exception as e:
        print('An error occurred:', e)

# URL of the website you want to scrape
url = 'https://www.cricketworldcup.com/'

# Set the duration between each scrape in seconds (30 seconds in this case)
scrape_interval = 5

while True:
    # Call the function to scrape the website
    scrape_website(url)

    # Wait for the specified interval before scraping again
    time.sleep(scrape_interval)
