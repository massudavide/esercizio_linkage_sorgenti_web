from lxml import html
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
import numpy as np
import pandas as pd
import operator

def main():
    source1 = loadSource("dataset/nba.txt")
    source2 = loadSource("dataset/rotoworld.txt")
    corpus1 = buildCorpus(source1)
    corpus2 = buildCorpus(source2)
    df1 = tfidfModel(corpus1)
    df2 = tfidfModel(corpus2)

    # da implementare
    # se un elemento del corpus è presente nella parte finale
    # dell'url quell'elemento peserà di più (x1.25)

    df1, df2 = (colonneComuni(df1, df2))

    df1 = annullaTermComTfIdf(df1)
    df2 = annullaTermComTfIdf(df2)

    df1, df2 = (colonneComuni(df1, df2))

    listaCoppiePagineDf1 = trova_pag_corrisp(df1, df2)
    listaCoppiePagineDf2 = trova_pag_corrisp(df2, df1)

    # print(listaCoppiePagineDf1)
    # print(listaCoppiePagineDf2)

    listaFinale = inters_liste(listaCoppiePagineDf1, listaCoppiePagineDf2)
    stampa_url(listaFinale, source1, source2)

# dati due df costruisce una lista di parole importanti per df1
# e somma gli elem corrisp in df2 ritornando una lista di liste con
# l'indice df1 e il corrisponte indice di df2
def trova_pag_corrisp(df1, df2):
    return allineaPagine(impElemList(df1), df2)


# ritorna una lista con le coppie indice dei due df che hanno matchato (stessa coppia)
# in tutte e due le liste
def inters_liste(lista1, lista2):
    listaFinale = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i][0] == lista2[j][1] and lista1[i][1] == lista2[j][0]:
                listaFinale.append(lista1[i])
    return listaFinale

# data una lista e due sorgenti, stampa gli url corrispondenti ad ogni coppia nella lista
def stampa_url(lista, source1, source2):
    for i in range(len(lista)):
        print('indice source1: ', lista[i][0], 'indice source2:', lista[i][1], '\n')
        print(source1[lista[i][0]],'  <--->  ', source2[lista[i][1]])


# data una lista di liste contenenti le parole più importanti, cerca nel df qual'è l'indice con sommatoria maggiore per ogni lista di parole date
# e ritorna una lista di liste contenente l'indice del df corrisp alle parole e l'indice del secondo df che ha dato risultato maggiore
# es: [[2,0],[1,2],[0,1]]
def allineaPagine(list, df):
    listaPagine = []
    for i in range(len(list)):
        listaPagine.append([i, indice_corrisp(df[list[i]])])
    return listaPagine

# dato un df somma tutti gli elementi sulle righe e ritorna l'indice maggiore
def indice_corrisp(df):
    dict = {}
    for i in df.T:
        dict[i] = sum_df_col(df.T[i])
    indice, maxValue = maximum_keys(dict)
    return indice

# somma tutti gli elem della riga
def sum_df_col(row):
    return row.sum()

# dato un df, per ogni riga aggiungi in lista tutte le parole con peso maggiore di 0
# ritorna una lista di liste i cui elem sono gli elem con peso maggiore di 0 per ogni riga
# es [['john', 'wall'],['luguentz', 'dort'],...]
def impElemList(df):
    list = []
    for i in df.T.columns:
        list2 = []
        for index, row in df.T.iterrows():
            if row[i] > 0.0:
                list2.append(index)
        list.append(list2)
    #print(list)
    return list

# ritorna indice e key del max elem del dizionario
def maximum_keys(dict):
    indice = max(dict, key=dict.get)
    max_val = dict[indice]
    return indice, max_val


# rimuovi tutte le colonne che hanno valori tutti con stesso peso e tutte le colonne che non contengono almeno uno 0
def annullaTermComTfIdf(df):
    list = []
    for i in df.columns:
        if not all_equal(df[i]) and not_all_positive(df[i]):
            list.append(i)
    return df[list]

# ritorna True se tutti gli elem sono uguali
def all_equal(iterator):
    return len(set(iterator)) <= 1

# ritorna true se vi è almeno uno 0
def not_all_positive(iterator):
    for i in iterator:
        if i == 0:
            return True


# def max15elem(df):
#     return df.apply(lambda x: pd.Series(np.concatenate([x.nlargest(15).index.values, x.nsmallest(0).index.values])), axis=1)


# ritorna soltanto le colonne comuni ai due df
def colonneComuni(df1, df2):
    lista_col_comuni = df1.columns.intersection(df2.columns)
    return df1[lista_col_comuni], df2[lista_col_comuni]

# given a list of url, returns a corpus of leaves
def buildCorpus(urlList):
    corpus = list()
    for url in range(len(urlList)):
        leaves = getLeaves(urlList[url])
        stringa = ''.join(map(str,leaves))
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
    file = open(filename,"r")
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

if __name__ == "__main__":
    main()
