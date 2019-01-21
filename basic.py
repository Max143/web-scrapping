

import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

url = 'https://stackoverflow.com/'

site = requests.get(url)

soup = BeautifulSoup(site.content, 'lxml')


   

# Getting the title/URLs/Votes/Views/Answers/asked by/person reputation score using find and find_all()/findAll
def findall():
    questions = soup.find_all(class_='question-summary')

    for que in questions:
        title = que.find(class_='question-hyperlink').get_text()
        print("Title: ", title)
        url = que.find(class_='question-hyperlink').get('href')
        print("Link: ", url)
        views = que.find(class_='views').find(class_='mini-counts').find('span').get_text()
        print("Views: ", views)
        answers = que.find(class_='status').find(class_='mini-counts').find('span').get_text()
        print("Answers: ", answers)
        asked_by = que.find(class_='summary').find(class_='started').get_text()
        print("Asked By: ", asked_by)
        

lst = []  # Empty list to store all data that we have scraped


# Getting the title/URLs/Votes/Views/Answers/asked by Using CSS selectors
def select():
    questions = soup.select('.question-summary')  # We have used here CSS selectors called select
    # Looping 
    for que in questions:
        title = que.select('.question-hyperlink')[0].get_text()
        print("Title: ", title)
        url = que.select('.question-hyperlink')[0]['href']     
        print('Link: ',  url)
        views = que.select('.views .mini-counts span')[0].get_text()
        print("Views: ", views)
        answers = que.select('.status .mini-counts span')[0].get_text()
        print("Answers: ", answers)
        asked_by = que.select('.summary .started')[0].get_text()
        print("Asked By: ", asked_by)

        # Passing data into dictionary
        data = {'title':title, 'url':url, 'views':views, 'answers':answers, 'asked_by':asked_by}
        lst.append(data)  # Appending data into empty lst

        






       
#driver code
# Uncomment Below see all data scraped

#findall()
#select()


# Saving all data csv file

select()




























