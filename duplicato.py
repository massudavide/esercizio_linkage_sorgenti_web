from lxml import html
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from sklearn.feature_extraction.text import TfidfVectorizer



page1 = requests.get('https://www.rotoworld.com/basketball/nba/player/29574/john-wall')
page2 = requests.get('https://www.rotoworld.com/basketball/nba/player/51073/luguentz-dort')
#page3 = requests.get('https://www.rotoworld.com/basketball/nba/player/29378/danilo-gallinari')

tree1 = html.fromstring(page1.content)
tree2 = html.fromstring(page2.content)
#tree3 = html.fromstring(page3.content)

text1 = tree1.xpath('//*[not(child::*)]/text()')
text2 = tree2.xpath('//*[not(child::*)]/text()')
#text3 = tree3.xpath('//*[not(child::*)]/text()')

# using list comprehension
stringa1 = ' '.join(map(str, text1))
stringa2 = ' '.join(map(str, text2))

corpus = [stringa1, stringa2]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)

