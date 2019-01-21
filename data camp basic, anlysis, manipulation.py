'''
BeautifulSoup Document
'''

import requests
from bs4 import BeautifulSoup

url = 'http://startuprly.com/'

webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, 'lxml')


print(soup.prettify())  # will get you complete html page in proper manner

print(soup.title)  # Return title with html tag

print(soup.title.string) # return title without html tag

# print(soup.parent.name)


print(soup.p)

print(soup.p['class'])

print(soup.a)

print(soup.find_all('a'))
