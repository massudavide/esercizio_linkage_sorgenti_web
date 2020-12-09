import requests
from lxml import html
import sys

# given a page url, returns all leaves of that page
def getLeaves(url):
    #print("Extracting leaves on: ", url)
    all_leaves = list()
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException:
            print("Could not find or page is unavailable with url: ", url)
            return all_leaves
    tree = html.fromstring(page.content)
    all_leaves = tree.xpath('//*[not(child::*)]/text()')
    return all_leaves

# given an input with filename, returns a list of url
def loadSource(filename):
    try:
        print("Opening file with path: ", filename)
        file = open(filename,"r")
    except OSError:
        print("Could not open/read file with path: ", filename)
        sys.exit()
    urlList = list()
    rows = file.readlines()
    for r in rows:
        if r not in urlList:
            urlList.append(r)
    file.close()        
    return urlList

# given a list of url, returns a corpus of leaves
def buildCorpus(urlList):
    corpus = list()
    for url in range(len(urlList)):
        leaves = getLeaves(urlList[url])
        stringa = ''.join(map(str,leaves))
        corpus.append(stringa)
    return corpus