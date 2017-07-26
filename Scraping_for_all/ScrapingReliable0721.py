import requests
from bs4 import BeautifulSoup
import dateutil.parser as parser
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
    
    def __init__(self, article , title , author , originalcontent , createddate , fetcheddate , articleurl , lastused ):
        self.Article = article
        self.Title = title
        self.OriginalContent = originalcontent
        self.CreatedDate = createddate
        self.FetchedDate = fetcheddate
        self.ArticleUrl = articleurl
        self.LastUsed = lastused
        self.Author = author
        
def scraping(href):
    headers = {'user-agent' : 'Mozilla/5.0'}
    if (requests.get(href, headers = headers)):
        source = requests.get(href, headers = headers)
        if (BeautifulSoup(source.content, "lxml")):
            soup = BeautifulSoup(source.content, "lxml").body 
            news = News(None, None, None, None, None, None, None, None)
            date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            news.fetchedDate = date
            news.lastUsed = date 
            news.articleUrl = href
            
            class_list_main = [    
                        'col-md-12',
                        'content-wrapper clearfix detail-block-md',
                        'entry-content',
                        'column column-two-third site-content',
                        'large-8 medium-12 columns first',
                        'article',
                        'article_body'
                        'container',
                        'span8',
                        'primary',
                        'l-container',
                        'row',
                        'story theme-main   '
            ]
            
            for i in range(len(class_list_main)):
                if (soup.findAll("",{'class':class_list_main[i]})):
#                     print(class_list_main[i])
                    content_list = soup.findAll("",{'class':class_list_main[i]})
                    for content in content_list:
                        scrape_details(content,news)
                        break
                else:
                    content = soup
                    scrape_details(content,news)
    
            print ('URL********************************************************')
            print (news.articleUrl)
            print ('TITLE********************************************************')
            print (news.title)
            print ('DATE********************************************************')
            print (news.createdDate)
            print ('AUTHOR********************************************************')
            print (news.author)
            print ('ARTICLE********************************************************')
            print (news.article) 
        else:
            print ('can not get the information!')
    else:
        print ('can not connect to the web page!')
              


# In[30]:

def scrape_details(content,news):  
    news.content = content
    class_list_title = [
                'entry-title',
                'entry-title single-title',
                'col-lg-9 col-md-8',
                'name post-title entry-title',
                'articleTitle',
                'artTitle',
                'blog-title',
                'postarea',
                'full-page-article left-col',
                'post_title',
                'post-title',
                'pg-headline',
                'content-header ',
                'field-subhead',
                '_8UFs4BVE',
                'headline'
            ] 
    for i in range(len(class_list_title)):
        if (content.find('',{'class':class_list_title[i]})):
#             print (class_list_title[i])
            news.title = content.find('',{'class':class_list_title[i]}).text         
            break
        else:
            news.title = None

    class_list_paragraph = [
                'ArticleBody__articleBody___1GSGP',
                'art-postcontent',
                'articles2',
                'article-inner',
                'article-text',                    
                'article-content',
                'article-copy',
                'article_body',
                'articleContentData',
                'b-item__description',
                'content-main',
                'content-text', 
                'entry-content clearfix',
                'entry-content full-content',
                'entry clearfix',        
                'entry-content', 
                'entry_content',
                'entry-content print-only',
                'entry-body',
                'entry',                                       
                'entry entry-content',
                'event-text', 
                'entry-content-text',
                'field-item even',
                'field-body',
                'infopage-news',
                'td-post-content', 
                'the-content cf',
                'thecontent',
                'td-post-content td-pb-padding-side',
                'ntText',                          
                'post-single',                     
                'post-content entry-content cf',   
                'post-body entry-content',        
                'post_entry',                      
                'post-content clearfix', 
                'post-bodycopy clearfix',
                'post-single-content box mark-links',
                'post-9141 post type-post status-publish format-standard has-post-thumbnail hentry category-world tag-fake-news tag-featured tag-satire',
                'vw-post-content clearfix',
                'wpb_wrapper',
                'single-box clearfix entry-content',
                'story-body story-body-1',
                'sqs-block-content',
                'left relative',
                'metadata__byline__author',
                'row'
    ]

    news.article = []
    for i in range(len(class_list_paragraph)):
        if (content.find('div',{'class': class_list_paragraph[i]})): 
#             print (class_list_paragraph[i])
            paragraphs = content.find('',{'class': class_list_paragraph[i]})
            if (paragraphs.findAll('p')):
                for paragraph in paragraphs.findAll('p'):
                    news.article.append(paragraph.text)
                break
        else:    
            news.article = []

    class_list_author = [
                'postmetadata',
                'author-article-link',
                'field-author',
                'name',
                'url fn n',
                'author vcard',
                'author left-edge',
                'author has-bio',
                'author',
                'artAuthor',
                'post-author',
                'meta pf-author',
                'author-name vcard fn',
                'text font-accent color-brand size-1x-small _1HynphR0',
                'byline-author'
    ]

    for i in range(len(class_list_author)):
        if (content.find('',{'class': class_list_author[i]})):
#             print (class_list_author[i])
            news.author = content.find("",{'class':class_list_author[i]}).text 
            break
        else:
            news.author = None


    class_list_date = [
                'entry-date published',
                'entry-date published updated',
                'content-published-mobile',
                'entry-date',
                'entry-meta',
                'entry-meta-date updated',
                'byline byline-left ',
                'pub_date',
                'post-date updated',
                'timestamp',
                'time',
                'article-details',
                'article_date',
                'artData',
                'field-post-date',
                'update-time',
                'row text font-accent size-1x-small color-darker-gray',
                'dateline'
    ]

    for i in range(len(class_list_date)):
        if (content.find('',{'class': class_list_date[i]})):
#             print(class_list_date[i])
            news.createdDate = content.find('',{'class': class_list_date[i]})
            try:
                news.createdDate = (parser.parse(news.createdDate['datetime'])).isoformat()
            except:
                news.createdDate = (parser.parse(news.createdDate.text)).isoformat()
            break
        else:
            news.createdDate = None

    return
link = 'https://www.nytimes.com/2017/07/20/arts/music/chester-bennington-linkin-park-dead.html'

scraping(link)
