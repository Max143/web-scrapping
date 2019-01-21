import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.positivityblog.com/'

webpage  = requests.get(url)

soup = BeautifulSoup(webpage.text, 'lxml')

# Getting the title of the web page
print("Title of the Website: ",soup.title.string)

print("-----------------------")


# Grab the Post
posts = soup.find_all(class_='post_box grt')

for post in posts:
    title = post.find(class_='headline')
    print(title)
