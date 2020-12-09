def corrisp_url(df1, df2):
    listaCoppiePagineDf1 = trova_pag_corrisp(df1, df2)
    listaCoppiePagineDf2 = trova_pag_corrisp(df2, df1)
    listaFinale = inters_liste(listaCoppiePagineDf1, listaCoppiePagineDf2)
    return listaFinale


# dati due df costruisce una lista di parole importanti per df1
# e somma gli elem corrisp in df2 ritornando una lista di liste con
# l'indice df1 e il corrisponte indice di df2
def trova_pag_corrisp(df1, df2):
    elem_imp = impElemList(df1)
    return allineaPagine(elem_imp, df2)

# ritorna una lista con le coppie indice dei due df che hanno matchato (stessa coppia)
# in tutte e due le liste
def inters_liste(lista1, lista2):
    listaFinale = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i][0] == lista2[j][1] and lista1[i][1] == lista2[j][0]:
                listaFinale.append(lista1[i])
    return listaFinale

# dato un df, per ogni riga aggiungi in lista tutte le parole con peso maggiore di 0.6
# ritorna una lista di liste i cui elem sono gli elem con peso maggiore di 0.6 per ogni riga
# es [['john', 'wall'],['luguentz', 'dort'],...]
def impElemList(df):
    list = []
    for i in df.T:
        list2 = []
        dfT = df.T
        for index, row in dfT.iterrows():
            if row[i] > 0.06:
                list2.append(index)
        list.append(list2)
    #print(list)
    return list

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

# ritorna indice e key del max elem del dizionario
def maximum_keys(dict):
    indice = max(dict, key=dict.get)
    max_val = dict[indice]
    return indice, max_val