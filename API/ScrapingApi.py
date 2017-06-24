
# coding: utf-8


import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import db

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


def get_news_content(href):
    headers = {'user-agent' : 'Mozilla/5.0'}
    try:
        source = requests.get(href, headers = headers)
    except requests.exceptions.ConnectionError:
        source.status_code = "Connection refused"
    if source.status_code == 200: 
        soup = BeautifulSoup(source.content, "lxml").body
        
        # print ("\nArticle Url: \n")
        print (href)
        
        # print("\nArticle: \n")  
        if (soup.findAll('p')):
            for article in soup.findAll('p'):
                article = article.text
        else:
            article = 'Unknown'
#             print (article)

        # print ("\nFetched Date: \n")
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        fetchedDate = date
        # print (fetchedDate)
                
        # print ("\nLast Used: \n")
        lastUsed = date
        # print (lastUsed)
        
        # print ("\nOriginal Content: \n")
        orginalContent = source.content
#         print (orginalContent)
        
        # print ("\nTitle: \n")
        if (soup.findAll('h1')):
            for title in soup.findAll('h1'):
                title = title.text
        else:
            title = 'Unknown'
        # print (title)

        
#    if the website is theguardian        
        if (urlparse(href).netloc) == 'www.theguardian.com':
            # print ("\nCreated Date: \n")
            if (soup.find('time')):
                for createdDate in soup.findAll('time'):
                    createdDate = createdDate.text
            else:
                createdDate = 'Unknown'
            # print (createdDate)
       
            # print ("\nAuthor: \n")
            if(soup.findAll('a', {'class':'tone-colour'})):
                for author in soup.findAll('a', {'class':'tone-colour'}):
                    author = author.text
            else:
                author = 'Unknown'
            # print(author)
 

#     if the website is bbc
        elif (urlparse(href).netloc) == 'www.bbc.co.uk':
            # print ("\nCreated Data: \n")
            if (soup.find('div', {'class': 'date date--v2'})):
                for createdDate in soup.findAll('div', {'class': 'date date--v2'}):
                    createdDate = createdDate.text
            else: 
                createdDate = 'Unknown'
            # print (createdDate)
       
            # print ("\nAuthor: \n")
            if (soup.findAll('a', {'class':'tone-colour'})):
                for author in soup.findAll('a', {'class':'tone-colour'}):
                    author = author.text
            else:
                author = 'Unknown'
            # print(author)
 

#     if the website is abc
        elif (urlparse(href).netloc) == 'www.abc.net.au':
            # print ("\nCreated Data: \n")
            if (soup.find('span', {'class': 'timestamp'})):
                createdDate = soup.find('span', {'class': 'timestamp'}).text
            else:
                createdDate = 'Unknown'
            # print (createdDate)
           
            # print ("\nAuthor: \n")
            if (soup.find('a', {'target':'_self'})):
                author = soup.find('a', {'target':'_self'}).text
            else:
                author = 'Unknown'
            # print(author)


#      if the website is cnn   
        elif (urlparse(href).netloc) == 'www.cnn.com':
            # print ("\nCreated Data: \n")
            if (soup.find('p', {'class': 'update-time'})):
                createdDate = soup.find('p', {'class': 'update-time'}).text
            else:
                createdDate = 'Unknown'
            # print (createdDate)
       
    
            # print ("\nAuthor: \n")
            if (soup.find('span', {'class':'metadata__byline__author'})):
                for author in soup.find('span', {'class':'metadata__byline__author'}):
                    author = author.string
            else:
                author = 'Unknown'
            # print(author)


#    if the website is indepedent
        elif (urlparse(href).netloc) == 'www.independent.co.uk':
            # print ("\nCreated Data: \n")
            if (soup.find('time')):
                createdDate = soup.find('time').text
            else:
                createdDate = 'Unknown'
            # print (createdDate)
    
            # print ("\nAuthor: \n")
            if (soup.find('span', {'itemprop':'name'})):
                for author in soup.find('span', {'itemprop':'name'}):
                    author = author.string
            else:
                author = 'Unknown'
            # print(author)


#   if the website is reuters
        elif (urlparse(href).netloc) == 'www.reuters.com':
            # print ("\nCreated Data: \n")
            if (soup.find('span', {'class': 'timestamp'})):
                createdDate = soup.find('span', {'class': 'timestamp'}).text
            else:
                createdDate = 'Unknown'
            # print (createdDate)
          
            # print ("\nAuthor: \n")
            if (soup.find('span', {'class':'author'})):
                for author in soup.find('span', {'class':'author'}):
                    author = author.string
            else: 
                author = 'Unknown'
            # print(author)
 

#   if the website is time
        elif (urlparse(href).netloc) == 'time.com':
            # print ("\nCreated Data: \n")
            if (soup.find('div', {'class': 'row text font-accent size-1x-small color-darker-gray'})):
                createdDate = soup.find('div', {'class': 'row text font-accent size-1x-small color-darker-gray'}).text
            else: 
                createdDate = 'Unknown'
            # print (createdDate)
          
            # print ("\nAuthor: \n")
            if (soup.find('a', {'class':'text font-accent color-brand size-1x-small _1HynphR0'})):
                for author in soup.find('a', {'class':'text font-accent color-brand size-1x-small _1HynphR0'}):
                    author = author.string
            else: 
                author = 'Unknown'
            # print(author)
            
        else:
            createdDate = 'Unknown'
            author = 'Unknown'

    else:
        title = 'Unknown'
        article = 'Unknown'
        author = 'Unknown'
        orginalContent  = 'Unknown'
        createdDate = 'Unknown'
        date = 'Unknown'
        href = 'Unknown'
        date  = 'Unknown'

    news = News(title, article, author, orginalContent, createdDate, date, href, date)
    db.uploadDBNews(news)




