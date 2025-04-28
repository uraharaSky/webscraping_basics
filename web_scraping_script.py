import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    "User-agents" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

##Creating lists for storing data
Product_reviews = []
Product_name = []
Product_cost = []
Product_rating = []

##Creating loop for Pagination
for i in range(1,24):
    url = 'https://www.flipkart.com/search?q=mobile+phones+&amp;otracker=search&amp;otracker1=search&amp;marketplace=FLIPKART&amp;as-show=on&amp;as=off&amp;page=' + str(i)

    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')

    print(request)

