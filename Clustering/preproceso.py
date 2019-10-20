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
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF
#from gensim.models import Word2Vec                                   #For Word2Vec

nltk.download('punkt')
#nltk.download('popular')

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
        self.asignarTemaArticulo(articulo)
        self.asignarLugarArticulo(articulo)

    ### funciones ###
    def asignarTemaArticulo(self, articulo):
        """ funcion que asugna la etiqueta tema del articulo """
        for tema in articulo.find_all("topics"):
            un_tema = tema.text.encode('utf-8', 'ignore')
            self.temas.append(un_tema)
            Datos.etiquetas_temas_sitios.add(un_tema)

    def asignarLugarArticulo(self, articulo):
        """ funcion que asugna la etiqueta lugar del articulo """
        for sitios in articulo.find_all("places"):
            un_lugar = sitios.text.encode('utf-8', 'ignore')
            self.sitios.append(un_lugar)
            Datos.etiquetas_temas_sitios.add(un_lugar)

    def aumentar_lista_dicc(self, articulo):
        """ crea una lista de tokens de las palabras del titulo/cuerpo """
        texto = articulo.find('text')
        titulo = texto.title
        cuerpo = texto.body
        boolEtiqueta = False
        if titulo != None:
            self.palabras.title = self.tokenizacion(titulo.text, boolEtiqueta)
        if cuerpo != None:
            self.palabras.body = self.tokenizacion(cuerpo.text, boolEtiqueta)

    def tokenizacion(self, texto, bool_etiquetas = False):
        """ crea la lista de palabras que analizaremos  """
        # quita digitos y puntuacion
        sin_num = texto.translate(string.digits)
        sin_punt = sin_num.translate(string.punctuation)
        """pruebas no funciona con lo de abajo"""
        #text = texto.encode("utf8").translate(None, string.digits).decode("utf8")
        #sin_puntuacion = text.encode("utf8").translate(None, string.punctuation).decode("utf8")

        # separar el texto en tokens
        tokens = nltk.word_tokenize(sin_punt)
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

    def __init__(self):
        self.vector = []

    def generar_vector_de_un_texto(self,texto):
        vectorizer = TfidfVectorizer()
        vector = self.vectorizer.fit_transform(texto)
        return vector

    def generar_TF_IDF(self, docs):
        vectorizer = TfidfVectorizer()
        self.vector = vectorizer.fit_transform(docs)

#######################################################################
#            funciones del preproceso, cargar los archivos            #
#######################################################################
def scrap_texto(texto_plano):
    return BeautifulSoup(texto_plano, "html.parser")

def escanear_docs(directorio):
    pares = dict([])
    documentos = []
    for fichero in os.listdir(directorio):
        # abrir los archivos 'xxx.sgm' de un directorio
        docs = open(os.path.join(directorio, fichero), 'r')
        texto = docs.read()
        docs.close()
        bsoup = scrap_texto(texto.lower())
        for reuter in bsoup.find_all("reuters"):
            articulo = Datos(reuter)
            pares[articulo] = reuter

        for document, reuter in pares.items():
            document.aumentar_lista_dicc(reuter)
            documentos.append(document)
        print ("Se ha terminado de examinar el fichero:", fichero)
    return documentos

def preprocesar():
    directorio = 'datos'
    print('\nGenerando los vectores de las instancias')
    documentos = escanear_docs(directorio)
    # generate lexicon of unique words for feature reduction
    print('Feature vector generation complete. Preprocessing phase complete!')
    return documentos