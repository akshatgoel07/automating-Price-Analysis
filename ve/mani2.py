from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
search_bar.send_keys("item name")
search_bar.send_keys(Keys.ENTER)

time.sleep(20) # wait for the search results to load

# flipkart_price_str = driver.find_element(By.CSS_SELECTOR, "._1vC4OE._2rQ-NK").text
# flipkart_price = float(flipkart_price_str.replace(',', '').replace('₹', ''))

driver.get("https://www.amazon.com")
search_bar = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_bar.send_keys("item name")
search_bar.send_keys(Keys.ENTER)

time.sleep(20)
amazon_price_str = driver.find_element(By.CSS_SELECTOR, ".s-result-item:nth-child(1) .a-offscreen").text
amazon_price = float(amazon_price_str.replace('$', ''))

if amazon_price < flipkart_price:
    print("Amazon has the better price!")
else:
    print("Flipkart has the better price!")

# Close the browser
driver.quit()
