from bs4 import BeautifulSoup;
import requests;
import csv;
from collections import Counter



page_to_scrape = requests.get("https://timesofindia.indiatimes.com/astrology/horoscope/horoscope-today-march-31-2024-read-your-daily-astrological-predictions/articleshow/108871244.cms")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

search_term = ["Aries", "Taurus","Gemini", "Cancer","Leo", "Virgo","Libra","Scorpio", "Sagittarius","Capricorn", "Aquarius","Pisces"]
txt = soup.br.parent.get_text(strip=True, separator="\n")
durations = ["Mar 21 - Apr 19","Apr 20 - May 20","May 21 - Jun 20","Jun 21 - Jul 22","Jul 23 - Aug 22","Aug 23 - Sep 22","Sep 23 - Oct 22",
             "Oct 23 - Nov 21	","Nov 22 - Dec 21","Dec 22 - Jan 19","Jan 20 - Feb 18","Feb 19 - March 20"]
end=len(txt)
start=0
arr = []
i=0
file=open("scrape.csv", "w")
writer = csv.writer(file)
writer.writerow(["Zodiac","Duration","Day"])

for term in search_term :
   pos = txt.find(term) 
   arr.append(pos)


for term,duration, a in zip(search_term,durations, arr):
   newpos = a+len(term)
   if(i >= len(arr)-1):
      print(term+"==="+txt[newpos: len(txt)])
      writer.writerow([term,duration,txt[newpos: len(txt)]])      
   else:
      print(term+"==="+txt[newpos: arr[i+1]])
      writer.writerow([term,duration,txt[newpos: arr[i+1]]])
   i=i+1
   
  
  