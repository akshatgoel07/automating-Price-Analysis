from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
driver.get("https://www.flipkart.com")
search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
search_bar.send_keys("sony headphones")
search_bar.send_keys(Keys.ENTER)

time.sleep(10) # wait for the search results to load

flipkart_price_element = driver.find_element(By.XPATH, "//div[contains(@class, '_1vC4OE') and contains(@class, '_2rQ-NK')]")
flipkart_price = flipkart_price_element.text
print(flipkart_price)
# driver.get("https://www.amazon.in")
# search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
# search_bar.send_keys("sony headphones")
# search_bar.send_keys(Keys.ENTER)

# time.sleep(5)

# amazon_price_element = driver.find_element(By.XPATH, "//span[contains(@class, 'a-price-whole')]")
# amazon_price = amazon_price_element.text.replace(',', '')

# if int(amazon_price) < int(flipkart_price):
#     print("Amazon has the better price!")
# else:
#     print("Flipkart has the better price!")

driver.quit()
