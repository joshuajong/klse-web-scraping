import pdb
import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://klse.i3investor.com/servlets/stk/1155.jsp'
pdb.set_trace()
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

last_price = soup.find('p', text='Last Price').find_next('strong').get_text()

# Extract data
print("Last price is: RM" + last_price)
