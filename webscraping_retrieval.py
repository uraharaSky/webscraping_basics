import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.flipkart.com/",
    "Connection": "keep-alive"
}

url = "https://www.flipkart.com/search?q=mobile+phonmes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"

response = requests.get(url, headers=headers)

with open("Flipkart.html", "w", encoding="utf-8") as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all("div", class_="tUxRFH")

for product in products:

     # Product name
    product_name = product.find("div", class_="KzDlHZ").text
    product_price = product.find("div", class_="Nx9bqj _4b5DiR").text
    product_ratings = product.find("div", class_="XQDdHH").text
    product_image = product.find("img", class_="DByuf4")["src"]

    print(product_name)
    print(product_price)
    print(product_ratings)
    print(product_image)
    print("-"*60)

