
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
    print(href)
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
                        'article'
            ]
            
            for i in range(len(class_list_main)):
                if (soup.findAll("",{'class':class_list_main[i]})):
#                     print(class_list_main[i])
                    content_list = soup.findAll("",{'class':class_list_main[i]})
#                     print (content_list)
                    for content in content_list:
                        scrape_details(content,news)
            print (news.title)
            print (news.createdDate)
            print (news.author)
            print (news.article)
            print (news.fetchedDate)
            print (news.lastUsed)
            print (news.articleUrl)
                
              


# In[389]:

def scrape_details(content,news):            
    news.content = content
    class_list_title = [
                'entry-title',
                'entry-title single-title',
                'col-lg-9 col-md-8',
                'name post-title entry-title',
                'articleTitle',
                'blog-title',
                'postarea',
                'full-page-article left-col',
                'post_title',
                'post-title',
                'content-header '
            ]
    title = None 
    for i in range(len(class_list_title)):
        if (content.find('',{'class':class_list_title[i]})):
            news.title = content.find('',{'class':class_list_title[i]}).text
            break


    class_list_paragraph = [
                'ArticleBody__articleBody___1GSGP',
                'art-postcontent',
                'articles2',
                'article-inner',
                'article-text',                    
                'article-content',                
                'b-item__description',
                'content-main',
                'content-text', 
                'content',
                'entry-content clearfix',
                'entry-content full-content',
                'entry clearfix',        
                'entry-content', 
                'entry_content',
                'entry-body',
                'entry',                                       
                'entry entry-content',
                'event-text', 
                'entry-content-text',
                'field-item even',
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
                'sqs-block-content',
    ]
    
    news.article = []
    for i in range(len(class_list_paragraph)):
        if (content.find('div',{'class': class_list_paragraph[i]})):  
            paragraphs = content.find('',{'class': class_list_paragraph[i]})
            if (paragraphs.findAll('p')):
                for paragraph in paragraphs.findAll('p'):
                    news.article.append(paragraph.text)
                break
    


    class_list_author = [
                'postmetadata',
                'author-article-link',
                'field-author',
                'fn',
                'name',
                'url fn n',
                'author vcard'
    ]
    
    for i in range(len(class_list_author)):
        if (content.find('',{'class': class_list_author[i]})):
            news.author = content.find("",{'class':class_list_author[i]}).text 
            break
   
    class_list_date = [
                'entry-date published',
                'entry-date published updated',
                'content-published-mobile',
                'entry-date',
                'byline byline-left ',
                'pub_date'
    ]
    
    for i in range(len(class_list_date)):
        while (content.find('',{'class': class_list_date[i]})):
#             print(class_list_date[i])
            news.createdDate = content.find('',{'class': class_list_date[i]})
            news.createdDate = (parser.parse(news.createdDate.text)).isoformat()
#             news.createdDate = (parser.parse(news.createdDate['datetime'])).isoformat()
            break


    return



link = 'http://www.thedailysheeple.com/astronomers-detect-strange-radio-signals-from-nearby-star_072017'
# link = 'http://americannews.com/hollywood-liberal-alyssa-milano-throws-rocks-trump-hits-hillary-obama-instead/'
scraping(link)


