import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XD9SXlwzbIU'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id='seven-day-forecast')

forcast_items = seven_day.find_all(class_='tombstone-container')

tonight = forcast_items[0]


# Extracting information from the page
print("Extracting information from the page")

img = tonight.find("img")
desc = img['title']

print("Title: ",desc) 

period = tonight.find(class_='period-name').get_text()
print(period)

desc = tonight.find(class_='short-desc').get_text()
print(desc)

temp = tonight.find(class_="temp").get_text()
print(temp)

print("-----------------------------")

# Extracting all the information from the page
print('Extracting all the information from the page')

period_tags = seven_day.select(".tombstone-container .period-name")

periods = [pt.get_text() for pt in period_tags]
print(periods)

# We can apply the same technique to get the other 3 fields

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)


print("--------------------------------------")

weather = pd.DataFrame({
    "period" : periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs 
    })


print(weather)



















