import requests
from bs4 import BeautifulSoup

# Send a request to the URL and get the HTML content
url = "https://bonitasmokeshop.com/arturo-fuente-don-carlos-double-robusto/"
response = requests.get(url)
html_content = response.content

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find the price elements and extract the current and MSRP prices
current_price = soup.find("span", {"class": "price price--withoutTax"}).text.strip()
msrp_price = soup.find("span", {"class": "price price--rrp"}).text.strip()
print("Current Price:", current_price)
print("MSRP Price:", msrp_price)

#Use this format to scrape prices off of our site.