from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
driver.get("https://www.flipkart.com")
search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
search_bar.send_keys("sony headphones whch720phones")
search_bar.send_keys(Keys.ENTER)

time.sleep(5) # wait for the search results to load
# flipkart_price = driver.find_element(By.CSS_SELECTOR, "._1vC4OE._2rQ-NK").text  
# //*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]

# flipkart_price_element = driver.find_element(By.XPATH, "//div[contains(@class, '_1vC4OE') and contains(@class, '_2rQ-NK')]")
# flipkart_price = flipkart_price_element.text


driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
driver.get("https://www.amazon.in")
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("sony headphones whch720phones")
search_bar.send_keys(Keys.ENTER)



time.sleep(20)
amazon_price = driver.find_element(By.CSS_SELECTOR, ".s-result-item:nth-child(1) .a-offscreen").text
print(amazon_price)



# if amazon_price < flipkart_price:
#     print("Amazon has the better price!")
# else:
#     print("Flipkart has the better price!")

# Close the browser
driver.quit()
