
# coding: utf-8

# In[43]:

import dateutil.parser as parser
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
import re
import datetime


# In[46]:

def scoring (news):
    article = news.Article
    createdDate = news.CreatedDate
    title = news.Title
    author = news.Author
    originalContent = news.OriginalContent
    lastUsed = news.LastUsed
    href = news.ArticleUrl
    fetchedDate = news.FetchedDate
    
    print (href)
    
    score = 0
    
    if (title):
        score += 1
        
    if (article):
        list_number = []
        score_para = 0
        for paragraphs in article:
            length = len(re.findall(r'\w+', paragraphs))
            list_number.append(length)
        max_number = max(list_number)
#         print (max_number)
        if (max_number <= 100):
            score += 1
    
    if (createdDate):
        createdDate_str = datetime.datetime.strptime(createdDate, "%Y-%m-%dT%H:%M:%S")
        fetchedDate_str = datetime.datetime.strptime(fetchedDate, "%Y-%m-%dT%H:%M:%S")    
        duration = fetchedDate_str - createdDate_str
        if (duration.days <= 5):
            score += 1
        elif (5 < duration.days < 10):
            score += 0.5
        
    if (author):
        score += 1
    
    if (lastUsed):
        score += 1
    
    if (fetchedDate):
        score += 1
        
    print ('********total:**********', score)


# In[47]:


class News:
    Article = []
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
    for i in range(len(link)):
        link[i] = 'http://' + link[i]
        headers = {'user-agent' : 'Mozilla/5.0'}            
        try:
            source = requests.get(link[i], headers = headers)
            soup = BeautifulSoup(source.content, "lxml")
        except requests.exceptions.ConnectionError:
            print ('Connection refused!!!')
        
        
        if (soup.findAll('article')):
            for article in soup.findAll('article'):
                if (article.find('a')):
                    href = article.find('a').get('href')
                    if href.startswith('http'):
                        href = href
                    else:
                        href = link[i] + href
                    get_news_content(href)
                else:
                    print ('not able to get <a>!!')
        else: 
            print ('not able to get <article>!!')
        
    
 
def get_news_content(href):
    headers = {'user-agent' : 'Mozilla/5.0'}
    try:
        source = requests.get(href, headers = headers)
    except requests.exceptions.ConnectionError:
        source.status_code = "Connection refused"
    if (BeautifulSoup(source.content, "lxml").body):
        soup = BeautifulSoup(source.content, "lxml").body
        if (soup.findAll('p')):            
            article = []
            for paragraph in soup.findAll('p'):
                article.append(paragraph.text)
        else:
            article = 'Unknown'
        date = time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(time.time()))
        fetchedDate = date
        lastUsed = date        
        orginalContent = source.content
        
        
        if (urlparse(href).netloc == 'americannews.com'):              
            if (soup.findAll('h1')):
                for title in soup.findAll('h1'):
                    title = title.text
            else:
                title = 'Unknown'        
            if (soup.find('time',{'class': 'rpwe-time published'})):
                createdDate = soup.find('time',{'class': 'rpwe-time published'}).text
                createdDate = (parser.parse(createdDate)).isoformat()
            else: 
                createdDate = None  

            if (soup.findAll('b')):
                for author in soup.findAll('b'):
                    author = author.text
            else:
                author = 'Unknown'
        
        elif (urlparse(href).netloc == 'www.activistpost.com'):
            if (soup.findAll('span', {'class': 'entry-meta-date updated'})):
                for createdDate in soup.findAll('span', {'class': 'entry-meta-date updated'}):
                    createdDate = (parser.parse(createdDate.text)).isoformat()
            else:
                createdDate = None

            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            
            for authors in soup.findAll('p'):
                if (authors.findAll('a')):
                    for author in authors.findAll('a'):
                        author = author.text
                else: 
                    author = 'Unknown'
        
        
        
        elif (urlparse(href).netloc == 'www.thedailysheeple.com'):
            if (soup.findAll('time', {'class': 'entry-date'})):
                for createdDate in soup.findAll('time', {'class': 'entry-date'}):
                    createdDate = (parser.parse(createdDate.text)).isoformat()
            else:
                createdDate = None

                
            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            
        
        
        elif (urlparse(href).netloc == 'waterfordwhispersnews.com'):
            if (soup.findAll('p', {'class': 'byline byline-left '})):
                for createdDate in soup.findAll('p', {'class': 'byline byline-left '}):
                    # createdDate = (parser.parse(createdDate.text)).isoformat()
                    createdDate = None
            else:
                createdDate = None
                
            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'

        
        
        elif (urlparse(href).netloc == 'www.clickhole.com'):

            if (soup.findAll('div', {'class': 'pub_date'})):
                for createdDate in soup.findAll('div', {'class': 'pub_date'}):
                    createdDate = (parser.parse(createdDate.text)).isoformat()
            else:
                createdDate = None

            if (soup.findAll('h1', {'class': 'headline'})):
                for title in soup.findAll('h1', {'class': 'headline'}):
                    title = title.text
            else:
                title = 'Unknown'

            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'

        
        elif (urlparse(href).netloc == 'theonion.com'):
            if (soup.findAll('span', {'class': 'content-published-mobile'})):
                for createdDate in soup.findAll('span', {'class': 'content-published-mobile'}):
                    createdDate = (parser.parse(createdDate.text)).isoformat()
            else:
                createdDate = None
            
            if (soup.findAll('header', {'class': 'content-header'})):
                for title in soup.findAll('header', {'class': 'content-header'}):
                    title = title.text
            else:
                title = 'Unknown'
            
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
                        
        else:
            title = 'Unknown'
            author = 'Unknown'
            createdDate = None
    else:
        print ('can not get connent')
        return
    news = News(article, title, author, orginalContent, createdDate, date, href, date)
    scoring(news)
    
link = [
        'thedailysheeple.com',
#         'waterfordwhispersnews.com',
#         'clickhole.com',
#         'americannews.com',
#         'activistpost.com',
#         'theonion.com'
        ]

get_news_firstpage(link)


# In[ ]:




# In[ ]:



