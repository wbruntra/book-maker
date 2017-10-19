from bs4 import BeautifulSoup as Soup
import codecs

# with codecs.open('pages/different-worlds.htm','r',encoding='utf8') as f:
#     content = f.read()

def parse_page(html):
    soup = Soup(html, 'html5lib')
    o = dict()
    o["title"] = (soup.h1.text).strip()
    o["date"] = (soup.find('span',{"class":"entry-date"})).text.strip()
    o["link"] = (soup.find('a', {"rel":"bookmark"}))['href']
    post_content = (soup.find('div', {"class":"pjgm-postcontent"}))
    try:
        post_content.find('div', {"class":"sharedaddy"}).decompose()
    except:
        pass
    o["post_content"] = post_content.prettify(formatter="html")
    return o

def make_chapter_html(chapter):
    title = "<h1>{}</h1>".format(chapter['title'])
    date = "<h3>{}</h3>".format(chapter['date'])
    link = "<h4><a href={}>Link</a></h4>".format(chapter['link'])
    html = '\n'.join([title, date, link, chapter['post_content'], link ])
    return html

# parsed = parse_page(content)
