

import urllib.request
import requests
import json

import requests
from bs4 import BeautifulSoup
import time
import traceback
# import psycopg2
import datetime

# connectionString = "dbname='correctdb' user='postgres' host='localhost' password='ucdcsngl'"
# conn = psycopg2.connect(connectionString)

def uploadDBNewsApi(newsApi):
    print ('store in api db')

    # try:

    #     cur = conn.cursor()


    #     # publishedAt = time.mktime(datetime.datetime.strptime(PublishedAt, "%Y-%m-%d").timetuple())

    #     cur.execute("INSERT INTO NewsFetchedApi (Url, Author, Title, Description, ImageUrl, PublishedAt) VALUES (%s, %s, %s, %s, %s, %s)", (Url, Author, Title, Description, ImageUrl, PublishedAt))
    #     conn.commit();
    #     cur.close()

    # except psycopg2.Error as e:
    #     print("I am unable to connect to the database")
    #     print(e)
    #     print(e.pgcode)
    #     print(e.pgerror)
    #     print(traceback.format_exc())
    # return



def uploadDBNews(news):
    print ('store in news db')

    # try:

    #     cur = conn.cursor()

    #     # createdDate = time.mktime(datetime.datetime.strptime(CreatedDate, "%d/%m/%Y").timetuple())
    #     # fetchedDate = time.mktime(datetime.datetime.strptime(FetchedDate, "%d/%m/%Y").timetuple())
    #     # lastUsed = time.mktime(datetime.datetime.strptime(LastUsed, "%d/%m/%Y").timetuple())


    #     cur.execute("INSERT INTO News (Article, Title, Author, OriginalContent, CreatedDate, FetchedDate,ArticleUrl,LastUsed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (news.Article, news.Title, news.Author, news.OriginalContent, news.CreatedDate, news.FetchedDate, news.ArticleUrl, news.LastUsed))
    #     conn.commit();
    #     cur.close()

    # except psycopg2.Error as e:
    #     print("I am unable to connect to the database")
    #     print(e)
    #     print(e.pgcode)
    #     print(e.pgerror)
    #     print(traceback.format_exc())
    # return



# class News:
#     Article = ''
#     Title = ''
#     Author = ''
#     OriginalContent = ''
#     CreatedDate = ''
#     FetchedDate = ''
#     ArticleUrl = ''
#     LastUsed = ''

#     def __init__(self, article , title, author, originalcontent, createddate, fetcheddate, articleurl, lastused):
#         self.Article = article
#         self.Title = title
#         self.OriginalContent = originalcontent
#         self.CreatedDate = createddate
#         self.FetchedDate = fetcheddate
#         self.ArticleUrl = articleurl
#         self.LastUsed = lastused
#         self.Author = author

    
# def get_news_firstpage(link):
#     link = 'http://' + link
#     print (link)
#     headers = {'user-agent' : 'Mozilla/5.0'}
#     source = requests.get(link, headers = headers)
#     if source.status_code == 200:
#         soup = BeautifulSoup(source.content, "lxml")
#     else:
#         print ("Oops, the website can not be found!!!")

#     for article in soup.findAll('article'):
#         href = article.find('a').get('href')
#         if href.startswith('http'):
#             print (href)
#         else:
#             href = link + href
#         get_news_content(href)

# def get_news_content(href):
#     headers = {'user-agent' : 'Mozilla/5.0'}
#     try:
#         source = requests.get(href, headers = headers)
#     except requests.exceptions.ConnectionError:
#         source.status_code = "Connection refused"
#     if source.status_code == 200:
#         soup = BeautifulSoup(source.content, "lxml").body

#         print ("\nTitle: \n")
#         for title in soup.findAll('h1'):
#             print (title.text)

#         print("\nArticle: \n")
#         for article in soup.findAll('p'):
#             print (article.text)

#         print ("\nFetched Date: \n")
#         date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#         print (date)

#         print ("\nArticle Url: \n")
#         print (href)

#         print ("\nLast Used: \n")
#         print (date)

#         print ("\nOriginal Content: \n")
#         print (source.content)

#         print ("\nCreated Data: \n")
#         for createdDate in soup.find('time',{'class': 'rpwe-time published'}):
#             print (createdDate)

#         print ("\nAuthor: \n")
#         for author in soup.findAll('b'):
#             print(author.text)

#     else:
#         print ("Oops, the web page can not be found!!!")

# news = News(title.text, article.text, author.text, source.content, createdDate, date, href, date)
#     uploadDBNews(news)


# link = 'americannews.com'
# get_news_firstpage(link)

