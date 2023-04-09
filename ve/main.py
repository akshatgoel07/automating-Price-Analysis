from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
time.sleep(5)
search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
search_bar.send_keys("sony whch720n")
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
headphone = driver.find_element(By.CSS_SELECTOR,"._30jeq3")
print( "Flipkart" ,headphone.text)

time.sleep(5)


driver.get("https://www.amazon.in")
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("sony whch720n")
search_bar.send_keys(Keys.ENTER)
headphone = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]/span[2]")
print("Amazon",headphone.text)



# if amazon_price < flipkart_price:
#     print("Amazon has the better price!")
# else:
#     print("Flipkart has the better price!")

# Close the browser
driver.quit()
