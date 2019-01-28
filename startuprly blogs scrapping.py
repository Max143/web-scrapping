    import requests
from bs4 import BeautifulSoup

url = 'http://startuprly.com/simplified-blogs/'

site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')



count = 0

print("Title: ", soup.title.string)

contents = soup.find('div', class_='article-grid-container')



posts = contents.find_all('article', "post-content")

for post in posts:
    title = post.find('header', class_='entry-header').find('h2',class_='entry-title')
    print("Blog Title: ", title.a.text)
    date = post.find('h5', class_='entry-date')
    print("Published Date: ",date.string)
    count += 1
    print("---------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")


    

print("Total Blogs: ", count)
''''
Testing as a single object -
# I can scrape single data easily 
single_post = posts[0]

title = single_post.find('h2', class_='post-card-title')
print(title.string)

date = single_post.find('span', class_='post-card-date')
print(date.string)

tags = single_post.find('span', class_='post-card-tags')
print(tags.string)

'''
    

    






 





