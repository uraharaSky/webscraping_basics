from bs4 import BeautifulSoup
import requests
import time
import sqlite3

conn = sqlite3.connect('flipkart_products_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                name TEXT,
                price TEXT,
                ratings TEXT,
                image_url TEXT                                         
                 )
              ''')

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.flipkart.com/",
    "Connection": "keep-alive"
}

for page in range(1, 20):
    url = "https://www.flipkart.com/search?q=mobile+phonmes&amp;otracker=search&amp;otracker1=search&amp;marketplace=FLIPKART&amp;as-show=on&amp;as=off&amp;as-pos=1&amp;as-type=HISTORY&amp;page={page}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all("div", class_="tUxRFH")

    for product in products:
        try:
            name = product.find("div", class_="KzDlHZ").text.strip()
            price = product.find("div", class_="Nx9bqj _4b5DiR").text.strip()
            ratings = product.find("div", class_="XQDdHH").text.strip()
            image_url = product.find("img", class_="DByuf4")["src"]

            cursor.execute("INSERT INTO products (name, price, ratings, image_url) VALUES (?, ?, ?, ?)",
                           (name, price, ratings, image_url))
        except Exception as e:
            print("Error due to missing product values", e)

    time.sleep(5)

conn.commit()
conn.close()

print("Scraping completed and data saved to SQLite.")

