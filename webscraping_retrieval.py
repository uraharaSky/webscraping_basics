import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.flipkart.com/",
    "Connection": "keep-alive"
}

name, price, ratings, image_url = [], [], [], []

for page in range(1, 11):
    url = "https://www.flipkart.com/search?q=mobile+phonmes&amp;otracker=search&amp;otracker1=search&amp;marketplace=FLIPKART&amp;as-show=on&amp;as=off&amp;as-pos=1&amp;as-type=HISTORY&amp;page={page}"

    response = requests.get(url, headers=headers)
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

time.sleep(5)

df = pd.DataFrame(
    {
        "name":name,
        "price":price,
        "ratings":ratings,
        "image_url":image_url
    }
)

with open(f"Flipkart_page_{page}.html", "w", encoding="utf-8") as file:
    file.write(response.text)

df.to_csv("flipkart_products.csv", index=False)

print(df)
