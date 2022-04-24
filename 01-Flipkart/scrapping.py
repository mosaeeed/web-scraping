# Import Libraries
from pydoc import describe
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# To configure webdriver to use Firefox browser, 
driver = webdriver.Firefox()

# Lists to store the rsult	
products = [] #List to store name of the product
prices = [] #List to store price of the product
discount_amount = []
payed_prices = []
description = [] #List to store rating of the product

# the openning url
driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq=")


# extract data from the website

## get the page content and save it 
content = driver.page_source
soup = BeautifulSoup(content , features='lxml')

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
     # pasrsing the info
    name = a.find('div', attrs={'class':'_4rR01T'})
    price = a.find('div', attrs={'class':'_3I9_wc _27UcVY'})
    discount = a.find('div', attrs={'class':'_3Ay6Sb'})
    payed = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    des = a.find('div', attrs={'class':'_1xgFaf'})
    # save the info in the list 
    products.append(name.get_text())
    discount_amount.append(discount.get_text())
    payed_prices.append(payed.get_text())
    prices.append(price.get_text())
    description.append(des.get_text()) 

driver.close()

# Store the data in a required format "CSV Formate"
df = pd.DataFrame({'Product Name':products, 'Price':prices, 'dicount':discount_amount,'paied preice':payed_prices , 'Description':describtion}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
print(df.head())
