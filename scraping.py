
# coding: utf-8

# In[110]:

import requests
from bs4 import BeautifulSoup
import time

class News:
    Article = ''
    Title = ''
    Author = ''
    OriginalContent = ''
    CreatedDate = ''
    FetchedDate = ''
    ArticleUrl = ''
    LastUsed = ''
    
    def __init__(self, article , title, author, originalcontent, createddate, fetcheddate, articleurl, lastused):
        self.Article = article
        self.Title = title
        self.OriginalContent = originalcontent
        self.CreatedDate = createddate
        self.FetchedDate = fetcheddate
        self.ArticleUrl = articleurl
        self.LastUsed = lastused
        self.Author = author


def get_news_firstpage(link):
    link = 'http://' + link
    print (link)
    headers = {'user-agent' : 'Mozilla/5.0'}
    source = requests.get(link, headers = headers)
    if source.status_code == 200: 
        soup = BeautifulSoup(source.content, "lxml")
    else: 
        print ("Oops, the website can not be found!!!")
    
    for article in soup.findAll('article'):
        href = article.find('a').get('href')
        if href.startswith('http'): # for activisitpost
            print (href)
        else:
            href = link + href
        get_news_content(href)
 
def get_news_content(href):
    headers = {'user-agent' : 'Mozilla/5.0'}
    try:
        source = requests.get(href, headers = headers)
    except requests.exceptions.ConnectionError:
        source.status_code = "Connection refused"
    if source.status_code == 200: 
        soup = BeautifulSoup(source.content, "lxml").body
        
        print ("\nTitle: \n")
        for title in soup.findAll('h1'):
            print (title.text)
        
        print("\nArticle: \n")        
        for article in soup.findAll('p'):
            print (article.text)

        print ("\nFetched Date: \n")
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print (date)
        
        print ("\nArticle Url: \n")
        print (href)
               
        print ("\nLast Used: \n")
        print (date)
        
        print ("\nOriginal Content: \n")
        print (source.content)
        
        print ("\nCreated Data: \n")
        for createdDate in soup.find('time',{'class': 'rpwe-time published'}):
            print (createdDate)
       
        print ("\nAuthor: \n")
        for author in soup.findAll('b'):
            print(author.text)
            
    else: 
        print ("Oops, the web page can not be found!!!")
        
    news = News(title.text, article.text, author.text, source.content, createdDate, date, href, date)

# link = 'activistpost.com'
link = 'americannews.com'
get_news_firstpage(link)



# In[ ]:




# In[ ]:



