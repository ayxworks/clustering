"""
Importar modulos y librerias
os: para interactuar con el sistema operativo
nltk: para procesar el texto (linguistica y tokenizacion)
string: para trabajr con el texto y encoding
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nltk
import string

from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF
#from gensim.models import Word2Vec                                   #For Word2Vec

### clases ###
class ListaDicc:
    def __init__(self):
        self.titulo = []
        self.cuerpo = []

class Datos:
    # Se guardan los temas y sitios, por si se quiere omitir en el clustering o no
    etiquetas_temas_sitios = set()

    def __init__(self, articulo):
        self.temas = []
        self.sitios = []
        self.palabras = ListaDicc()

        self.asignarDescripcionArticulo(articulo)

    ### funciones ###
    def asignarDescripcionArticulo(self, articulo):
        """ funcion que asugna la descripcion del articulo
        """
        for tema in articulo.temas.children:
            un_tema = tema.text.encode('utf-8', 'ignore')
            self.temas.append(un_tema)
            Datos.etiquetas_temas_sitios.add(un_tema)
        for sitios in articulo.sitios.children:
            un_lugar = sitios.text.encode('utf-8', 'ignore')
            self.temas.append(un_lugar)
            Datos.etiquetas_temas_sitios.add(un_lugar)

    def aumentar_lista_dicc(self, articulo):
        """ crea una lista de tokens de las palabras del titulo/cuerpo
        """
        texto = articulo.find('text')
        titulo = texto.title
        cuerpo = texto.body
        if titulo != None:
            self.palabras.title = self.tokenizacion(titulo.text)
        if cuerpo != None:
            self.palabras.body = self.tokenizacion(cuerpo.text)

    def tokenizacion(self, text, bool_etiquetas):
        """ crea la lista de palabras que analizaremos
            :returns: lista de tokens filtrados y generizados
        """
        utf = text.encode('utf-8', 'ignore')
        # quita digitos y puntuacion
        sin_digitos = utf.translate(None, string.digits)
        sin_puntuacion = sin_digitos.translate(None, string.punctuation)
        # separar el texto en tokens
        tokens = nltk.word_tokenize(sin_puntuacion)
        # quitar si el usuario quiere la 'clase'/etiquetas/temas, stop words y palabras que no sean en ingles
        sin_stop = [w for w in tokens if not w in stopwords.words('english')]
        if bool_etiquetas:
            clase_etiqueta_art = [w for w in sin_stop]
        else:
            clase_etiqueta_art = [w for w in sin_stop if not w in Datos.etiquetas_temas_sitios]

        eng = [y for y in clase_etiqueta_art if wordnet.synsets(y)]

        """
        !!!PARA MAS ADELANTE OBTENER RAICES!!!
        
        # lemmatization
        lemmas = []
        lmtzr = WordNetLemmatizer()
        for token in eng:
            lemmas.append(lmtzr.lemmatize(token))
        # stemming
        stems = []
        stemmer = PorterStemmer()
        for token in lemmas:
            stem = stemmer.stem(token).encode('utf-8', 'ignore')
            if len(stem) >= 4:
                stems.append(stem)
        return stems
        """
        return eng

class Tf_Idf:
    def __init__(self,documents):
        self.vector = []
        self.vectorizer = TfidfVectorizer()

    def generar_vector_de_un_texto(self,texto):
        vector = self.vectorizer.fit_transform(texto)
        return vector

    def generar_TF_IDF(self, docs):
        self.vector = self.vectorizer.fit_transform(docs)