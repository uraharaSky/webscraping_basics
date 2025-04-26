import pandas as pd
import requests
from bs4 import BeautifulSoup

baseurl = "https://www.flipkart.com"

request = requests.get(baseurl)
print(request)
