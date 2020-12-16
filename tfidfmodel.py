import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def esegui_tfIdf(corpus1, corpus2):
    df1 = tfidfModel(corpus1)
    df2 = tfidfModel(corpus2)

    df1, df2 = colonne_comuni(df1, df2)

    df1 = annulla_term_com_TfIdf(df1)
    df2 = annulla_term_com_TfIdf(df2)

    df1, df2 = colonne_comuni(df1, df2)

    df1 = increase_elem_value(df1)
    df2 = increase_elem_value(df2)


    return df1, df2

# given a corpus, returns a dataframe built with tf-idf model
def tfidfModel(corpus):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    denselist = X.todense().tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    return df

# ritorna il df con le colonne comuni ai due df
def colonne_comuni(df1, df2):
    lista_col_comuni = df1.columns.intersection(df2.columns)
    return df1[lista_col_comuni], df2[lista_col_comuni]

# rimuovi tutte le colonne che hanno valori tutti con stesso peso e tutte le colonne che non contengono almeno uno 0
def annulla_term_com_TfIdf(df):
    termini_rilevanti = []
    for i in df.columns:
        if not all_equal(df[i]) and not_all_positive(df[i]):
            termini_rilevanti.append(i)
    return df[termini_rilevanti]

# se nelle colonne è presente un solo valore diverso da 0, raddoppialo
def increase_elem_value(df):
    for i in df:
        if(len(set(df[i])) == 2):
            df[i] = df[i].apply(lambda x: x*2 if x != 0 else x)
    return df

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