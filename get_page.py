import requests
import codecs
from creds import headers
from bs4 import BeautifulSoup as Soup
import time
import os
from process_chapter import parse_page, make_chapter_html

def get_title_from_url(url):
    return url.split('/')[-2] + '.htm'

def get_page(url):
    title = get_title_from_url(url)
    filepath = os.path.join(os.getcwd(), 'pages', title)
    if not os.path.isfile(filepath):
        print(title + ' not found')
        r = requests.get(url, headers=headers)
        html = r.text
        save_page(url, html)
    else:
        print(title + ' exists')
        with codecs.open(filepath, 'r', encoding='utf8') as f:
            html = f.read()
    return html

def save_page(url, html):
    title = get_title_from_url(url)
    print('Saving page {}'.format(title))
    filepath = os.path.join(os.getcwd(), 'pages', title)
    with codecs.open(filepath, 'w', encoding='utf8') as f:
        f.write(html)
    time.sleep(1)


def get_content(html, el, params):
    soup = Soup(html, "html.parser")
    content = soup.find(el, params)
    return content

def get_links(url):
    r = requests.get(url, headers=headers)
    soup = Soup(r.text, "html.parser")
    links = []
    for a in soup.find_all('a'):
        link = a.get('href')
        if link:
            links.append(link)
    return links

# links_url = "http://slatestarcodex.com/archives/?comments=false"

# url = "http://slatestarcodex.com/2017/07/31/book-review-raise-a-genius/"

with codecs.open('filtered.txt','r',encoding='utf8') as f:
    links = f.read().split('\n')

links = [link + '?comments=false' for link in links]
book = []
for link in reversed(links[:10]):
    html = get_page(link)
    chapter = parse_page(html)
    book.append(make_chapter_html(chapter))

with codecs.open('book.htm','w',encoding='utf8') as f:
    f.write('\n'.join(book))

# el = 'div'
# params = {"class": "post"}

# html = get_page(url)
# content = get_content(html, el, params)
# with codecs.open('page.htm', 'w', encoding="utf8") as f:
#     f.write(content.prettify(formatter='html'))

# links = get_links(links_url)
# print(links)
# with codecs.open('archives.txt','w',encoding='utf8') as f:
#     f.write('\n'.join(links))
