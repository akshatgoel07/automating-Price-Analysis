from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.flipkart.com")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()
    time.sleep(5)
    search_bar = driver.find_element(By.CSS_SELECTOR, "._3704LK")
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    flipkart_headphone = driver.find_element(By.CSS_SELECTOR,"._30jeq3")
    flipkart_price = flipkart_headphone.text.replace('₹','').replace(',','')
    flipkart_model = flipkart_headphone.get_attribute('title')

    time.sleep(5)

    driver.get("https://www.amazon.in")
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    amazon_headphone = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[2]/span[2]")
    amazon_price = amazon_headphone.text.replace('₹','').replace(',','')
    amazon_model = amazon_headphone.get_attribute('aria-label')

    driver.quit()

    if int(amazon_price) < int(flipkart_price):
        better_price = "Amazon"
    else:
        better_price = "Flipkart"

    return render_template('results.html', query=query, flipkart_price=flipkart_price, flipkart_model=flipkart_model, amazon_price=amazon_price, amazon_model=amazon_model, better_price=better_price)


if __name__ == '__main__':
    app.run()
