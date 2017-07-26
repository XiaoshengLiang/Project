
# coding: utf-8

# In[11]:

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
    
def get_subUrl(href):
    print (href)
    headers = {'user-agent' : 'Mozilla/5.0'}
    if (requests.get(href, headers = headers)):
        source = requests.get(href, headers = headers)
        if (BeautifulSoup(source.content, "lxml").body):
            soup = BeautifulSoup(source.content, "lxml").body    
            
            class_list = [
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
                        'sqs-block-content'
            ]
        
            article = []
            subUrl_list = []
            for i in range(len(class_list)):
                while (soup.find('',{'class': class_list[i]})):   
                    paragraphs = soup.find('',{'class': class_list[i]})
                    if (paragraphs.findAll('p')):
                        for paragraph in paragraphs.findAll('p'):
                            if(paragraph.find('', href=True)):
                                subURL = paragraph.find('', href=True)['href']
                                if (subURL):
                                    subUrl_list.append(subURL)
                    break
            
        else:
            print ('can not get connent')
            return
    else:
        print ('Connection refused')
    return subUrl_list

href = 'http://www.thedailysheeple.com/aipac-friendly-bill-makes-boycotting-israel-a-felony-violators-could-spend-decades-in-jail_072017'
get_news_content(href)





# In[ ]:




# In[ ]:



