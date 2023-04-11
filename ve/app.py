from flask import Flask, request
from selenium import webdriver
from flask import jsonify
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search_headphone():
    search_query = request.json['data']['query']
    # Selenium code to search for headphone on Flipkart and Amazon
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.flipkart.com")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
    time.sleep(5)
    search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    flipkart_product_name = driver.find_element(By.CSS_SELECTOR, ".s1Q9rs").text
    flipkart_headphone = driver.find_element(By.CSS_SELECTOR,"._30jeq3")
    flipkart_price = int(flipkart_headphone.text.replace('₹','').replace(',',''))
    flipkart_link = driver.find_element(By.CSS_SELECTOR, '._2rpwqI').get_attribute('href')
    flipkart_product_image = driver.find_element(By.CSS_SELECTOR, "._396cs4").get_attribute('src')

    time.sleep(5)

    driver.get("https://www.amazon.in")
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.ENTER)
    amazon_product_name = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").text
    amazon_headphone = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]/span[2]")
    amazon_price = int(amazon_headphone.text.replace('₹','').replace(',',''))
    amazon_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a").get_attribute('href')
    amazon_product_image = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img").get_attribute('src')

    driver.quit()

    response =[
        {   
        'company': 'Flipkart',
        'product_name': flipkart_product_name,
        'price': flipkart_price,
        'link': flipkart_link,
        'product_image': flipkart_product_image
        },
        {
        'company': 'Amazon',
        'product_name': amazon_product_name,
        'price': amazon_price,
        'link': amazon_link,
        'product_image': amazon_product_image
        },
    ]
    sorted_response = sorted(response, key=lambda k: k['price'])
    return jsonify(sorted_response)

if __name__ == '__main__':
    app.run()