import wrapper as wr
import tfidfmodel as model
import pagealigner as aligner

def main():
    # basket
    source1 = wr.loadSource("dataset/basketball/rotoworld.txt")
    source2 = wr.loadSource("dataset/basketball/espn.txt")

    # libri
    # source1 = wr.loadSource("dataset/libri/ibs.txt")
    # source2 = wr.loadSource("dataset/libri/feltrinelli.txt")

    # tennis
    # source1 = wr.loadSource("dataset/tennis/atptour.txt")
    # source2 = wr.loadSource("dataset/tennis/eurosport.txt")

    # film
    # source1 = wr.loadSource("dataset/film/film.txt")
    # source2 = wr.loadSource("dataset/film/mymovies.txt")
    #
    corpus1 = wr.buildCorpus(source1)
    corpus2 = wr.buildCorpus(source2)

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
