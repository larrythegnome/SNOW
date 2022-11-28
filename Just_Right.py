import bs4
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.google.com/search?q=weather&rlz=1C1GCEA_enUS1032US1032&oq=weather&aqs=chrome..69i57j46i199i433i465i512j0i131i433i457i512j0i402l2j0i433i512j0i131i433i512l2j46i131i199i433i465i512j0i131i433i512.3009j1j7&sourceid=chrome&ie=UTF-8").content
 
soup = BeautifulSoup(html, 'html.parser')
tempGrab = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
temp = int(tempGrab [0:2])

if temp >= 90:
    print(f" ITS {temp}°F, THATS TOO HOT!")
elif temp > 65 < 90:
    print(f" ITS {temp}°F, THATS... Perfect")
if temp <= 65:
    print(f" ITS {temp}°F, THATS TOO COLD")