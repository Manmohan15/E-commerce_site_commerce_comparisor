from selenium import webdriver
import time
from pathlib import Path
product=input("Enter the product")
driver=webdriver.Chrome()

print("connecting to amazon.....")
amazon=driver.get('https://www.amazon.in/')
searchbar1=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbar1.send_keys(product)
search_btn=driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]')
search_btn.click()
time.sleep(2)
amazon_price=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/div/a/span[1]/span[2]/span[2]')
amazon_price=amazon_price.text


print("connecting to flipkart.....")
flipkart=driver.get('https://www.flipkart.com/')
close_btn=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
close_btn.click()
searchbar_flipkart=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchbar_flipkart.send_keys(product)
search_btn_flipkart=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_btn_flipkart.click()
time.sleep(2)
flipkart_price=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div')
flipkart_price=flipkart_price.text

print("The Product price at amazon is : "+amazon_price)
print("The Product price at flipkart is : "+flipkart_price)