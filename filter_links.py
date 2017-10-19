import re
import codecs
pattern = re.compile("\d+\/\d+\/\d+")

def is_open_thread(url):
    if 'open-thread' in url or re.search('ot\d+', url):
        print(url)
        return True
    return False

def ssc_filter(links):
    results = []
    for link in links:
        if re.search(pattern, link):
            if not is_open_thread(link):
                results.append(link)
    return results

with codecs.open('archives.txt','r',encoding='utf8') as f:
    links = f.read().split('\n')

links = ssc_filter(links)
with codecs.open('filtered.txt','w', encoding='utf8') as f:
    f.write('\n'.join(links))
