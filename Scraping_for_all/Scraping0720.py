
# coding: utf-8

# In[201]:

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
                        'span8'
            ]
            
            for i in range(len(class_list_main)):
                if (soup.findAll("",{'class':class_list_main[i]})):
#                     print(class_list_main[i])
                    content_list = soup.findAll("",{'class':class_list_main[i]})
#                     print (content_list)
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
              


# In[216]:

def scrape_details(content,news):  
    news.content = content
#         print (news.content)
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
                'content-header ',
                'field-subhead'
            ] 
    for i in range(len(class_list_title)):
        if (content.find('',{'class':class_list_title[i]})):
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
                'sqs-block-content',
                'left relative'
    ]

    news.article = []
    for i in range(len(class_list_paragraph)):
        if (content.find('div',{'class': class_list_paragraph[i]})): 
#             print (class_list_paragraph[i])
            paragraphs = content.find('',{'class': class_list_paragraph[i]})
            if (paragraphs.findAll('p')):
#                     print (paragraphs)
                for paragraph in paragraphs.findAll('p'):
                    news.article.append(paragraph.text)
#                     print (news.article)
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
                'author-name vcard fn'
    ]

    for i in range(len(class_list_author)):
        if (content.find('',{'class': class_list_author[i]})):
#             print (class_list_author[i])
            news.author = content.find("",{'class':class_list_author[i]}).text 
#             print (news.author)
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
    ]

    for i in range(len(class_list_date)):
        if (content.find('',{'class': class_list_date[i]})):
#             print(class_list_date[i])
            news.createdDate = content.find('',{'class': class_list_date[i]})
#             print (news.createdDate.text)
            try:
                news.createdDate = (parser.parse(news.createdDate['datetime'])).isoformat()
            except:
                news.createdDate = (parser.parse(news.createdDate.text)).isoformat()

            break
        else:
            news.createdDate = None

    return



# link = 'http://www.thedailysheeple.com/astronomers-detect-strange-radio-signals-from-nearby-star_072017'
# FAKE:
# link = 'http://awm.com/will-this-latest-blunder-be-the-final-nail-in-the-coffin-for-the-worst-show-in-tv-history/?utm_medium=homepage&utm_source=homepage1'
# link = 'http://americannews.com/beware-new-doll-meant-indoctrinate-sharia-law-children-coming-home/'
# UNRELIABLE:
# link = 'http://www.anonews.co/cop-drugs-frame/'
# link = 'http://anonhq.com/london-terror-attacks-brits-celebrating-beer-hero/'
# SATIRE
# link = 'http://empirenews.net/hillary-clinton-undergoes-sex-change-operation-so-she-has-a-better-chance-at-winning-2020-election/'
# link = 'http://realnewsrightnow.com/2017/05/texas-lawmaker-called-ice-mother-law-dinner-table-dispute/'
# Conspiracy:
# link = 'http://anotherdayintheempire.com/distraction-du-jour-trump-punches-cnn/'
# link = 'http://conservativefiringline.com/va-removes-top-2-officials-manchester-va-hospital/'
# HATE:
# link = 'http://www.frontpagemag.com/fpm/267321/nevertrump-nostalgia-hillary-never-was-daniel-greenfield'
# link = 'http://www.vdare.com/articles/said-in-spanish-dual-citizen-actress-activist-tells-illegals-how-not-to-get-arrested-a-new-app-for-dreamers-the-america-thing-etc'
# BIAS
# link = 'http://www.americanthinker.com/articles/2017/07/europe_downward_now_the_bavarians_want_to_leave.html'
# link = 'http://100percentfedup.com/watch-rep-steve-kings-bombshell-answer-trumps-wall-hasnt-built-yet-video/'
# Junk:
# link = 'http://www.celebtricity.com/nicki-minaj-files-10m-lawsuit-against-remy-ma-for-using-her-voice-in-diss-song-on-itunes/'
# link = 'https://www.scoopwhoop.com/india-inhuman-rape-cases/#.6j9dfreps'
# Political:
# link = 'http://thelastlineofdefense.org/breaking-president-trump-wants-you-to-know-the-truth-about-agenda-21/'
# link = 'http://www.defenddemocracy.press/one-week-after-mosuls-liberation-horror-of-us-siege-continues-to-unfold/'
# CLICKBAIT
# link = 'http://americablog.com/2017/07/cbo-gop-obamacare-repeal-22m-uninsured-13k-deductible-premiums-soar-older.html'
link = 'http://americanlookout.com/rms-corruption-more-obama-officials-scrutinized-in-unmasking-probe-video/'
scraping(link)


# In[ ]:




# In[ ]:



