import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"


print(f"Fetching data from: {url}...")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    print("Extracted Information ")
    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author_name = authors[i].text
        
        print(f"Quote {i+1}: {quote_text}")
        print(f"Author: {author_name}")
        
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")