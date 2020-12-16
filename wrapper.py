import requests
from lxml import html
import sys

# given a page url, returns all leaves of that page
def get_leaves(url):
    #print("Extracting leaves on: ", url)
    all_leaves = list()
    try:
        # page = requests.get((url, {'User-Agent': 'Mozilla/5.0'}))
        page = requests.get(url)
    except requests.exceptions.RequestException:
            print("Could not find or page is unavailable with url: ", url)
            return all_leaves
    tree = html.fromstring(page.content)
    all_leaves = tree.xpath('//*[not(child::*)]/text()')
    # print(url, all_leaves)
    return all_leaves

# given an input with filename, returns a list of url
def load_source(filename):
    try:
        print("Opening file with path: ", filename)
        file = open(filename,"r")
    except OSError:
        print("Could not open/read file with path: ", filename)
        sys.exit()
    url_list = list()
    rows = file.readlines()
    for r in rows:
        if r not in url_list:
            url_list.append(r)
    file.close()        
    return url_list

# given a list of url, returns a corpus of leaves
def build_corpus(url_list):
    corpus = list()
    for url in range(len(url_list)):
        leaves = get_leaves(url_list[url])
        stringa = ''.join(map(str,leaves))
        corpus.append(stringa)
    return corpus