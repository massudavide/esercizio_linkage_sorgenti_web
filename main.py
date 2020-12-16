import wrapper as wr
import tfidfmodel as model
import pagealigner as aligner
import pandas as pd
import numpy as np

def main():
    source1 = wr.load_source("dataset/nba.txt")
    source2 = wr.load_source("dataset/espn.txt")

    corpus1 = wr.build_corpus(source1)
    corpus2 = wr.build_corpus(source2)

    df1, df2 = model.esegui_tfIdf(corpus1, corpus2)

    lista_url = aligner.corrisp_url(df1, df2)
    stampa_url(lista_url, source1, source2)


# data una lista e due sorgenti, stampa gli url corrispondenti ad ogni coppia nella lista
def stampa_url(lista, source1, source2):
    print('numero pagine con corrispondenze: ', len(lista))
    for i in range(len(lista)):
        print('indice source1: ', lista[i][0], 'indice source2:', lista[i][1], '\n')
        print(source1[lista[i][0]], source2[lista[i][1]])

if __name__ == "__main__":
    main()
