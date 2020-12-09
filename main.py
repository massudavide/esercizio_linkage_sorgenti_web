import numpy as np
import pandas as pd
import operator

import wrapper as wr
import tfidfmodel as model
import pagealigner as aligner

def main():
    source1 = wr.loadSource("dataset/nba.txt")
    source2 = wr.loadSource("dataset/rotoworld.txt")
    corpus1 = wr.buildCorpus(source1)
    corpus2 = wr.buildCorpus(source2)

    df1 = model.tfidfModel(corpus1)
    df2 = model.tfidfModel(corpus2)

    df1, df2 = (model.colonneComuni(df1, df2))

    df1 = model.annullaTermComTfIdf(df1)
    df2 = model.annullaTermComTfIdf(df2)

    df1, df2 = (model.colonneComuni(df1, df2))

    df1 = model.increase_elem_value(df1)
    df2 = model.increase_elem_value(df2)

    listaCoppiePagineDf1 = aligner.trova_pag_corrisp(df1, df2)
    listaCoppiePagineDf2 = aligner.trova_pag_corrisp(df2, df1)
    listaFinale = aligner.inters_liste(listaCoppiePagineDf1, listaCoppiePagineDf2)
    
    stampa_url(listaFinale, source1, source2)

# data una lista e due sorgenti, stampa gli url corrispondenti ad ogni coppia nella lista
def stampa_url(lista, source1, source2):
    print('numero pagine corrispondinti: ', len(lista))
    for i in range(len(lista)):
        print('indice source1: ', lista[i][0], 'indice source2:', lista[i][1], '\n')
        print(source1[lista[i][0]], source2[lista[i][1]])

if __name__ == "__main__":
    main()
