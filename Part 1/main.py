from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
website = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"
count = 0

with open('part1.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews'])

    while count <= 20:
        driver.get(website+str(count+1))
        content = driver.page_source
        soup = BeautifulSoup(content,features="lxml")
        for data in soup.findAll('div', attrs={'class':'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16'}):
            try:
                product_url = data.find('a', href=True, attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href')
            except:
                product_url = None

            try:
                product_name = data.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'}).text
            except:
                product_name = None

            try:
                price = data.find('span', attrs={'class':'a-offscreen'}).text[1:]
            except:
                price = None

            try:
                rating = data.find('span', attrs={'class':'a-size-base puis-bold-weight-text'}).text
            except:
                rating = None
            
            for temp in data.find('div', attrs={'class':'a-row a-size-small'}):
                try:
                    reviews = temp.find('span', attrs={'class':'a-size-base'}).text[1:-1]
                except:
                    reviews = None
            
            writer.writerow([product_url, product_name, price, rating, reviews])

        count += 1
