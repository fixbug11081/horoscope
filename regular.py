
from bs4 import BeautifulSoup;
import requests;
import csv;


page_to_scrape = requests.get("https://www.horoscope.com/us/horoscopes/general/index-horoscope-general-daily.aspx")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
todays = soup.findAll("h3")
durations = soup.findAll("small")
zodiacs = soup.findAll("p")

file=open("scrape.csv", "w")
writer = csv.writer(file)
writer.writerow(["Zodiac","Duration","Day"])


for today ,duration, zodiac in zip(todays,durations, zodiacs):
   print(today.text +"-"+duration.text+"-"+ zodiac.text )
   writer.writerow([today.text,duration.text,zodiac.text])

