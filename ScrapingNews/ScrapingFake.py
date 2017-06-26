
# coding: utf-8



import requests
from bs4 import BeautifulSoup
import time
import ConnectDB
from urllib.parse import urlparse

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
    for i in range(len(link)):
        link[i] = 'http://' + link[i]
        headers = {'user-agent' : 'Mozilla/5.0'}            
        try:
            source = requests.get(link[i], headers = headers)
            soup = BeautifulSoup(source.content, "lxml")
            for article in soup.findAll('article'):
                href = article.find('a').get('href')
                if href.startswith('http'):
                    href = href
                else:
                    href = link + href
#                 print (href)
                get_news_content(href)
        except: 
            print ("Oops, the website can not be found!!!")

    
 
def get_news_content(href):
    headers = {'user-agent' : 'Mozilla/5.0'}
    try:
        source = requests.get(href, headers = headers)
    except requests.exceptions.ConnectionError:
        source.status_code = "Connection refused"
    if source.status_code == 200: 
        soup = BeautifulSoup(source.content, "lxml").body
        
#         print("\nArticle: \n")        
        if (soup.findAll('p')):
            for article in soup.findAll('p'):
                article = article.text
        else:
            article = 'Unknown'
#         print (article)

#         print ("\nFetched Date: \n")
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        fetchedDate = date
                
#         print ("\nLast Used: \n")
        lastUsed = date
#         print (lastUsed)
        
        
#         print ("\nArticle Url: \n")
        print (href)
        
#         print ("\nOriginal Content: \n")
        orginalContent = source.content
        
        
        if (urlparse(href).netloc == 'americannews.com'):              
            print ("\nTitle: \n")
            if (soup.findAll('h1')):
                for title in soup.findAll('h1'):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nCreated Data: \n")
            if (soup.find('time',{'class': 'rpwe-time published'})):
                createdDate = soup.find('time',{'class': 'rpwe-time published'}).text
            else: 
                createdDate = 'Unknown'
            print (createdDate)
       
            print ("\nAuthor: \n")
            if (soup.findAll('b')):
                for author in soup.findAll('b'):
                    author = author.text
            else:
                author = 'Unknown'
            print(author)
                    
         
    
        elif (urlparse(href).netloc == 'www.activistpost.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('span', {'class': 'entry-meta-date updated'})):
                for createdDate in soup.findAll('span', {'class': 'entry-meta-date updated'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            for authors in soup.findAll('p'):
                if (authors.findAll('a')):
                    for author in authors.findAll('a'):
                        author = author.text
                else: 
                    author = 'Unknown'
            print (author)
        
        
        
        elif (urlparse(href).netloc == 'www.thedailysheeple.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('time', {'class': 'entry-date'})):
                for createdDate in soup.findAll('time', {'class': 'entry-date'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            print (author)
            
        
        
        elif (urlparse(href).netloc == 'www.waterfordwhispersnews.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('p', {'class': 'byline byline-left'})):
                for createdDate in soup.findAll('p', {'class': 'byline byline-left'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('h1', {'class': 'entry-title'})):
                for title in soup.findAll('h1', {'class': 'entry-title'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            print (author)
        
        
        elif (urlparse(href).netloc == 'www.clickhole.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('div', {'class': 'pub_date'})):
                for createdDate in soup.findAll('div', {'class': 'pub_date'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('h1', {'class': 'headline'})):
                for title in soup.findAll('h1', {'class': 'headline'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            print (author)
        
        
        elif (urlparse(href).netloc == 'www.theonion.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('span', {'class': 'content-published-mobile'})):
                for createdDate in soup.findAll('span', {'class': 'content-published-mobile'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('header', {'class': 'content-header'})):
                for title in soup.findAll('header', {'class': 'content-header'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            print (author)
                
                
                
        elif (urlparse(href).netloc == 'www.thebeaverton.com'):
            print ("\nCreated Data: \n")
            if (soup.findAll('time', {'class': 'time'})):
                for createdDate in soup.findAll('timr', {'class': 'time'}):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            print (createdDate)
                
            print ("\nTitle: \n")
            if (soup.findAll('h3', {'class': 'headline'})):
                for title in soup.findAll('h3', {'class': 'headline'}):
                    title = title.text
            else:
                title = 'Unknown'
            print (title)
            
            print ("\nAuthor: \n")
            if (soup.findAll('span', {'class': 'author vcard'})):
                for author in soup.findAll('span', {'class': 'author vcard'}):
                    author = author.text
            else: 
                author = 'Unknown'
            print (author)
            
        else: 
            print ("Oops, the web page can not be found!!!")
            title = 'Unknown'
            author = 'Unknown'
            createdDate = 'Unknown'
                                                         
        
    news = News(title, article, author, orginalContent, createdDate, date, href, date)
    ConnectDB.uploadDBNews(news)


link = ['americannews.com',
       'activistpost.com',
       'thedailysheeple.com']

get_news_firstpage(link)







