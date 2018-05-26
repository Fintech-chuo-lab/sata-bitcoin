print("Hello world")
import requests
from bs4 import BeautifulSoup

print("Hello world")

target_url = "https://bitflyer.jp/?bf=hhbmzc42"

r = requests.get(target_url)

soup = BeautifulSoup(r.text,"html.parser")

buy_price = soup.select("#bfPriceBid_1")[0].string

print(buy_price)
