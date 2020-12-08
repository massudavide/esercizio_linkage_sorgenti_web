import requests
from lxml import html
from sklearn.feature_extraction.text import TfidfVectorizer

class Wrapper:

    # given a list of url, returns a corpus of leaves
    def buildCorpus(urlList):
        corpus = list()
        for url in range(len(urlList)):
            leaves = getLeaves(urlList[url])
            stringa = ''.join(map(str, leaves))
            corpus.append(stringa)
        return corpus

        # given a page url, returns all leaves of that page

    def getLeaves(url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        all_leaves = tree.xpath('//*[not(child::*)]/text()')
        return all_leaves

        # given an input with filename, returns a list of url

    def loadSource(filename):
        file = open(filename, "r")
        urlList = list()
        rows = file.readlines()
        for r in rows:
            urlList.append(r)
        return urlList

        # given a corpus, returns a dataframe built with tf-idf model

    def tfidfModel(corpus):
        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names()
        denselist = X.todense().tolist()
        df = pd.DataFrame(denselist, columns=feature_names)
        return df

        # DEPRECATED

    def getHTMLContent(url):
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        return soup.get_text()

    if __name__ == "__main__":
        main()