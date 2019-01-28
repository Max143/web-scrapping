# Task 1: Get Aticle Title, Tag, link, summary    -------------------------Done
# Task 2: Count the number of article present---------------------------Done
# Task 3: Get all the tag at one place------------------------------------Done


import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

url = 'https://www.dataquest.io/blog/tag/python/'

site = requests.get(url).text

soup = BeautifulSoup(site, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

# writing Columns header
csv_writer.writerow(['BLOG TITLE', 'TAG', 'SUMMARY', 'LINK'])

print("Website Title: ",soup.title.text)

print()
total_blogs = 0
all_tag = []


content = soup.find('div',class_='site-wrapper').find('main', class_='site-main outer').find('div', class_='inner')
posts = content.find('div', class_='post-feed')

articles = posts.find_all('article')

for article in articles:
    
    # Headline
    headline = article.h2.text
    print("Article Headline: ",headline)
    
    # Tag
    tags = article.find('span', class_='post-card-tags').text
    print("Article Tag: ", tags)
    if tags not in all_tag:
        all_tag.append(tags)

    # Summary
    summary = article.find('section').p.text
    print("Atrticle Summary: ", summary)

    # Link
    try:
        broken_link = article.find('a' ,class_='post-card-image-link')['href']
    except Exception as e:
        pass
        
    # Now, joining the broken link 
    link = ''.join(["https://www.dataquest.io", broken_link])  # To get the correct links
    print("Artilce Link: ", link)

    total_blogs += 1
    print()

print("-----------------------------------------")


# Total Blogs
print("Total Blogs: ", total_blogs)

# All tags
for tag in all_tag:
    print(tag) 

    
print("Saving Data into well-formated into CSV file")

csv_writer.writerow([headline, tags, summary, link])
csv_file.close()
    
# print(csv_writer)  Do not print becoz it will only generate position of csv_file in memory
    
    

