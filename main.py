from bs4 import BeautifulSoup
from lxml import html

# HTTP
import requests

# SELENIUM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://my.wealthsimple.com/app/login?locale=en-ca")

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
usernameTextbox = driver.find_element(By.XPATH, '//input[@type="text" and @spellcheck="false"]')

usernameTextbox.clear()

usernameTextbox.send_keys("mehmoodumar58")
driver.close()

paths = {
  "price": "//fin-streamer[@class='Fw(b) Fz(36px) Mb(-4px) D(ib)']"
}

stocks = {
  "TSLA": "https://finance.yahoo.com/quote/TSLA/",
  "GOOG": "https://finance.yahoo.com/quote/GOOG/"
}

r = requests.get(stocks["GOOG"])

soup = BeautifulSoup(r.content, 'html.parser')
root = html.fromstring(str(soup))
elements = root.xpath(paths["price"])

for element in elements:
    print(element.text)

def main():
  pass

if __name__ == "__main__":
  main()


