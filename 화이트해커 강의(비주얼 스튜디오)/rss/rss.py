import feedparser
import pandas as pd

url ="http://www.boannews.com/media/news_rss.xml?mkind=1"
feed = feedparser.parse(url)

titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description) 
    authors.append(entry.author)

data = {'제목':titles, '링크':links, '요약':descriptions, '작성자': authors}
df = pd.DataFrame(data)

df.to_excel('result_boannews.xlsx', index=False)