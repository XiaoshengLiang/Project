import requests
from bs4 import BeautifulSoup
import dateutil.parser as parser
import time
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
    try:
        source = requests.get(href, headers = headers)
        if source.status_code == 200:
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
                            'content content--article section-us-news tonal tonal--tone-news',
                            'entry-content',
                            'column column-two-third site-content',
                            'large-8 medium-12 columns first',
                            'article',
                            'article_body',
                            'Article_inner-container_SZATq',
                            'b-item',
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
            print ('Response is not 200!')
    except:
        print ('can not connect to the web page!')
              

def scrape_details(content, news):  
#     print (content)
    news.content = content
    class_list_title = [
                'ArticleHeader_headline_2zdFM',
                'articleheader',
                'article-title',
                'ArticleHeader__hed___GPB7e',
                'entry-title',
                'entry-title single-title',
                'col-lg-9 col-md-8',
                'content__headline',
                'name post-title entry-title',
                'articleTitle',
                'artTitle',
                'blog-title',
                'b-item__title',
                'postarea',
                'full-page-article left-col',
                'headline',
                'post_title',
                'post-title',
                'post-title entry-title',
                'post-headline',
                'pg-headline',
                'page-header',
                'content-header ',
                'field-subhead',
                '_8UFs4BVE',
                'headline',
                'title',
                'the-title',
                'single-title',
                'story-title',
                'xxlarge'
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
                'article',
                'ArticleBody_body_2ECha',
                'b-item__description',
                'blog-content clearfix',
                'blog-content',
                'content-main',
                'content-text', 
                'cb-entry-content clearfix',
                'content__article-body from-content-api js-article__body',
                'content',
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
                'entry-meta',
                'entry-content-text',
                'field-item even',
                'field-items',
                'field-body',
                'infopage-news',
                'inner-post-entry',
                'td-post-content', 
                'the-content cf',
                'thecontent',
                'text-wrapper',
                'td-post-content td-pb-padding-side',
                'ntText',  
                'new_block',
                'post-single',                     
                'post-content entry-content cf',   
                'post-body entry-content',        
                'post_entry',
                'post_content',
                'post-body',
                'post-content clearfix', 
                'post-bodycopy clearfix',
                'post-single-content box mark-links',
                'post-content',
                'post-9141 post type-post status-publish format-standard has-post-thumbnail hentry category-world tag-fake-news tag-featured tag-satire',
                'vw-post-content clearfix',
                'wpb_wrapper',
                'single-box clearfix entry-content',
                'story-body story-body-1',
                'story-content',
                'sqs-block-content',
                'single single-post postid-193191 single-format-standard',
                'left relative',
                'metadata__byline__author',
                'mainContent',
                'mk-single-content clearfix',
                'mvp-post-content-in',
                'group-container '
    ]

    news.article = []
    for i in range(len(class_list_paragraph)):
        if (content.find('',{'class': class_list_paragraph[i]})): 
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
                'author-section',
                'ArticleHeader_byline_1VRIx'
                'field-author',
                'field-items',
                'fn',
                'name',
                'url fn n',
                'author vcard',
                'author left-edge',
                'author has-bio',
                'author',
                'artAuthor',
                'post-author',
                'post_author',
                'meta pf-author',
                'meta-author',
                'meta-holder',
                'mk-author-name',
                'author-name vcard fn',
                'text font-accent color-brand size-1x-small _1HynphR0',
                'theauthor',
                'byline-author',
                'byline',
                'blog-author',
                'createdby',
                'cb-author',
                'username',
                'single-author',
                'small',
                'entry-author-name'
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
                'entry-meta-content',
                'entry-meta-date updated',
                'byline byline-left ',
                'bydate',
                'blog-date',
                'b-item__asked-by-time',
                'pub_date',
                'post-date',
                'post_date',
                'post-date updated',
                'published',
                'timestamp',
                'time',
                'article-details',
                'art-postheadericons art-metadata-icons',
                'article_date',
                'ArticleHeader_date_V9eGk',
                'ArticleTimestamp__timestamp___1klks',
                'artData',
                'cb-date',
                'field-post-date',
                'fa fa-clock-o',
                'update-time',
                'row text font-accent size-1x-small color-darker-gray',
                'dateline',
                'date',
                'dt-published date-callout',
                'content__dateline-lm js-lm u-h',
                'grDate',
                'submitted',
                'single-date',
                'mk-publish-date'
    ]

    for i in range(len(class_list_date)):
        if (content.find('',{'class': class_list_date[i]})):
#             print(class_list_date[i])
            news.createdDate = content.find('',{'class': class_list_date[i]})
            try:
                news.createdDate = (parser.parse(news.createdDate['datetime'])).isoformat()
            except:
                try:
                    news.createdDate = (parser.parse(news.createdDate.text)).isoformat()
                except:
                    news.createdDate = None
            break
        else:
            news.createdDate = None

    return

scraping(link)
