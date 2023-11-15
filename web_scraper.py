import pdb
import requests
from bs4 import BeautifulSoup

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def construct_url(stock_code, stock_name):
  return 'https://www.klsescreener.com/v2/stocks/view/' + str(stock_code) + '/' + stock_name + '.jsp'

def get_webpage(link):
    # Use headless mode to avoid opening a visible browser window
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    # Load the page
    driver.get(link)

    # Give the JavaScript on the page some time to execute
    time.sleep(5)

    # Get the page content after JavaScript has executed
    html = driver.page_source

    # Close the browser
    driver.quit()

    with open("allPriceTarget.html", "w") as myfile:
      myfile.write(html)

if __name__ == "__main__":
  get_webpage('https://www.klsescreener.com/v2/')
