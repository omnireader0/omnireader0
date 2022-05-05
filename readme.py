import feedparser

blog_rss_uri="https://sebiblog.tistory.com/rss"
feed = feedparser.parse(blog_rss_uri)

markdown_text = ""

j=0
for i in feed['entries']:
    j+= 1
    if j >5:
        break
    else:
        dt = i['published']
        markdown_text += f"[{i['title']}]({i['link']}) <br>\n"
        print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()  
