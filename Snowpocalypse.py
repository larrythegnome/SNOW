import re
from urllib import response
from bs4 import BeautifulSoup
from requests import get

URL = "https://weather.com/weather/tenday/l/Ohio+City+OH?canonicalCityId=679c5c3754e02b1d9ab03fd5af9a95899631aa81829a806f04d3dde1f15d9c2d"

response = get(URL)

soup = BeautifulSoup(response.text, "html.parser")

weather = soup.find_all("span")
snow = soup.find_all("Snowy")

for item in weather:
    print(item.text)

    print("BORING")

for item in snow:
    print("ITS GONNA SNOWWWWWW!!!!!!!")