import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190105035656&SearchText=leather+bag")

#soup = BeautifulSoup(r.content)
soup = soup.find_all("a")


print(soup)


