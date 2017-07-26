import datetime


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
        if (max_number <= 100):
            score += 1
    
    if (createdDate):
        createdDate_str = datetime.datetime.strptime(createdDate, "%Y-%m-%dT%H:%M:%S")
        fetchedDate_str = datetime.datetime.strptime(fetchedDate, "%Y-%m-%dT%H:%M:%S")    
        duration = fetchedDate_str - createdDate_str
        if (duration.days <= 5):
            score += 1
        
    if (author):
        score += 1
    
    if (lastUsed):
        score += 1
    
    if (fetchedDate):
        score += 1
        
    print ('********total:**********', score)


