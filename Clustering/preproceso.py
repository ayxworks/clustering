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

fichero_datos_vectores = ['datasets/dataset1.csv', 'datasets/dataset2.csv']

class Tf_Idf:
    def __init__(self, texto):
        self.vector = []
        self.tabla = dict([])
        self.generar_pesos(texto)

    def generar_pesos(self, texto):
        palabras, pesos = self.generar_TF_IDF(texto)
        array_de_pesos = pesos.toarray()
        for doc, row in enumerate(array_de_pesos):
            self.tabla[doc] = dict([])
            for i, palabra in enumerate(palabras):
                self.tabla[doc][palabra] = array_de_pesos[doc][i]

    def generar_TF_IDF(self, docs):
        palabras_dicc = dict([])
        for i, doc in enumerate(docs):
            palabras_dicc[i] = ' '.join(doc.words.title + doc.words.body)
        tfidf = TfidfVectorizer()
        pesos = tfidf.fit_transform(palabras_dicc.values())
        atributos = tfidf.get_feature_names()
        return atributos, pesos

"""
    def crear_dataset(self, docs, vocabulario):

        print 'Generando vector de atributos y dataset...'
        pesos = self.generar_pesos(docs)
        # generate feature list
        print('Selecting features for the feature vectors...')
        selector = FeatureSelector(pesos.tabla, docs)
        # write feature vectors to csv files
        for i, feature in enumerate(selector.features):
            print 'Writing feature vector data @', datafile[i]
            __generate_csv(fichero_datos_vectores[i], selector.features[i], selector.feature_vectors[i])
            print 'Finished generating dataset @', datafile[i]
        return selector.feature_vectors

    def __generate_csv(file, features, feature_vectors):
        # crea un csv con los vectores y las 'clases'/etiquetas
        # generate path if necessary
        path = os.path.join(os.getcwd(), 'datasets')
        if not os.path.isdir(path):
            os.makedirs(path)
        dataset_fichero_csv = open(file, "w")
        dataset_fichero_csv.write('id\t')
        for feature in features:
            dataset_fichero_csv.write(feature)
            dataset_fichero_csv.write('\t')
        dataset_fichero_csv.write('class-label:topics\t')
        dataset_fichero_csv.write('class-label:places\t')
        dataset_fichero_csv.write('\n')
        # feature vector for each document
        for i, feature_vector in feature_vectors.iteritems():
            # document id number
            dataset_fichero_csv.write(str(i))
            dataset_fichero_csv.write('\t')
            # each tf-idf score
            for score in feature_vector.vector:
                dataset_fichero_csv.write(str(score))
                dataset_fichero_csv.write('\t')
            # generate topic/places in fv
            dataset_fichero_csv.write(str(feature_vector.topics))
            dataset_fichero_csv.write(str(feature_vector.places))
            dataset_fichero_csv.write('\n')
        dataset_fichero_csv.close()
"""
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

        for articulo, reuter in pares.items():
            articulo.aumentar_lista_dicc(reuter)
            documentos.append(articulo)  #!TODO falla aqui, no entiendo por que se anaden cosas
        print("Se ha terminado de examinar el fichero:", fichero)
    return documentos

def preprocesar():
    directorio = 'datos'
    print('\nGenerando los vectores de las instancias')
    documentos = escanear_docs(directorio)
    #anadir todas las palabras de cada titulo y articulo en una estructura que tf_idf pueda leer
    #!TODO parece que no hay nada en documentos revisar, hay 1000 articulos y los detecta con len pero no consigo sacar las palabras
    texto_dicc = set()
    print("------------------------------------------------------------")
    #generar un diccionario de palabrtas que no se repiten (nuestro vocabulario)
    for articulo in documentos:
        print(articulo)
        for palabras in articulo.palabras.titulo:
            print(palabras)
            texto_dicc.add(palabras)
        for palabras in articulo.palabras.cuerpo:
            print(palabras)
            texto_dicc.add(palabras)
    print('Preproceso completado!')
    print(texto_dicc)
    return Tf_Idf(texto_dicc)