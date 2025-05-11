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

name, price, ratings, image_url = [], [], [], []

url = "https://www.flipkart.com/search?q=mobile+phonmes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"

response = requests.get(url, headers=headers)

with open("Flipkart.html", "w", encoding="utf-8") as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all("div", class_="tUxRFH")

for product in products:

     # Product name
    product_name = product.find("div", class_="KzDlHZ").text
    name.append(product_name)

     # Product price
    product_price = product.find("div", class_="Nx9bqj _4b5DiR").text
    price.append(product_price)

     #product ratings
    product_ratings = product.find("div", class_="XQDdHH").text
    ratings.append(product_ratings)

     #product image url
    product_image = product.find("img", class_="DByuf4")["src"]
    image_url.append(product_image)



df = pd.DataFrame(
    {
        "name":name,
        "price":price,
        "ratings":ratings,
        "image_url":image_url
    }
)


df.to_csv("flipkart_products.csv", index=False)

print(df)
