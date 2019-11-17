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
import random
import util
import pandas as pd     #trabajar con tablas/csv
from bs4 import BeautifulSoup
from operator import itemgetter
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF
from sklearn.feature_extraction.text import TfidfTransformer
#from gensim.models import Word2Vec                                   #For Word2Vec


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
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
        self.tema_numerico = []
        self.palabras = ListaDicc()
        self.articulo = ListaDicc()
        self.asignarTemaArticulo(articulo)
        self.asignarLugarArticulo(articulo)

    ### funciones ###
    def asignarTemaArticulo(self, articulo):
        """ funcion que asugna la etiqueta tema del articulo """
        for temas in articulo.find_all("topics"):
            for tema in temas:
                un_tema = tema.get_text()
                #un_tema = tema.text.encode('utf-8', 'ignore')
                self.temas.append(un_tema)
                Datos.etiquetas_temas_sitios.add(un_tema)

    def asignarLugarArticulo(self, articulo):
        """ funcion que asugna la etiqueta lugar del articulo """
        for sitios in articulo.find_all("places"):
            un_lugar = sitios.text.encode('utf-8', 'ignore')
            self.sitios.append(un_lugar)
            Datos.etiquetas_temas_sitios.add(un_lugar)

    def asignarTemaNumerico(self, lista_temas):
        """ funcion que asugna la etiqueta tema numerico para evaluacion del cluster """
        if self.temas == None:
            self.tema_numerico.append(0)
        for tema in self.temas:
            try:
                self.tema_numerico.append(lista_temas.index(tema))        
            except ValueError:
                print(tema + ' ,no esta en la lista y se ha añadido')
                lista_temas.append(tema)
                self.tema_numerico.append(lista_temas.index(tema))

    def aumentar_lista_dicc(self, articulo):
        """ crea una lista de tokens de las palabras del titulo/cuerpo """
        texto = articulo.find('text')
        titulo = texto.title
        cuerpo = texto.body
        boolEtiqueta = False
        if titulo != None:
            self.palabras.titulo = self.tokenizacion(titulo.text, boolEtiqueta)
            self.articulo.titulo = titulo.text
        if cuerpo != None:
            self.palabras.cuerpo = self.tokenizacion(cuerpo.text, boolEtiqueta)
            self.articulo.titulo = cuerpo.text

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

        # lemmatizacion
        lemmas = []
        lematizador = WordNetLemmatizer()
        for token in eng:
            lemmas.append(lematizador.lemmatize(token))
        # sacar raices
        raices = []
        saca_raices = PorterStemmer()
        for token in lemmas:
            raiz = saca_raices.stem(token).encode('utf-8', 'ignore')
            if len(raiz) >= 4:
                raices.append(raiz.decode('utf-8', 'ignore'))
        return raices

fichero_datos_vectores = ['datasets/dataset1.csv', 'datasets/dataset2.csv']

class Tf_Idf:
    def __init__(self):
        self.tfidf = TfidfVectorizer(max_df=0.9)
        self.vector = None
        self.atributos = []
        #self.vDocs = []

    def generar_vector_tupla_pesos(self, texto):
        vDocs = []
        listaVocab = dict([])
        palabras, pesos = self.generar_vocab_npalabras(texto, listaVocab)
        matriz_completa = pesos.toarray()
        for articulo, fila in enumerate(matriz_completa):
            doc = list()
            for i, palabra in enumerate(fila):
                doc.append(matriz_completa[articulo][i])
            vDocs.append(tuple(doc))
        self.vector = vDocs
        print("Lista de tuplas de vectores tf-idf generada")
        print("Se han procesado " + len(vDocs) + " instancias")
    
    def generar_vector_tupla_pesos_newInst(self, texto, listaVocab):
        vDocs = []
        palabras, pesos = self.generar_vocab_npalabras(texto, listaVocab)
        matriz_completa = pesos.toarray()
        for articulo, fila in enumerate(matriz_completa):
            doc = list()
            for i, palabra in enumerate(fila):
                doc.append(matriz_completa[articulo][i])
            vDocs.append(tuple(doc))
        self.vector = vDocs
        print("Lista de tuplas de vectores tf-idf generada")

    def generar_vocab_npalabras(self, docs, listaVocab):
        palabras_dicc = dict([])
        for i, doc in enumerate(docs):
            palabras_dicc[i] = ' '.join(doc.palabras.titulo + doc.palabras.cuerpo)
        listaVocab.update(palabras_dicc)
        util.guardar(os.getcwd()+"/preproceso/todas_las_palabras.txt" ,listaVocab)
        pesos = self.tfidf.fit_transform(listaVocab.values())
        self.vector = pesos
        atributos = self.tfidf.get_feature_names()
        self.atributos = atributos
        print("Espacio vectorial analizado y valores tf_idf calculados")
        return atributos, pesos

    def print_tabla(self):
        idf_trans=TfidfTransformer(smooth_idf=True,use_idf=True)
        idf_trans.fit(self.vector)
        # print idf values
        df_idf = pd.DataFrame(idf_trans.idf_, index=self.tfidf.get_feature_names(),columns=["idf_pesos"])
        # orden ascendente
        df_idf.sort_values(by=['idf_pesos'])

class SelectorAtributos:
    def __init__(self,pesos,documentos):
        """ 
            escoge los atributos y se genera un vector del espacio vectorial de las palabras de los articulos
            :param pesos: los pesos de tf_idf.vector
            :param docmuentos: lista de documentos
        """
        self.atributos = []
        self.espacio_vectorial = []
 
        self.elegirAtributos(pesos)
        for atributos_doc in self.atributos:
            self.crear_dataset(pesos,documentos,atributos_doc)

    def elegirAtributos(self,pesos):
        """ 
            genera un vector reducido de atributos
            :param pesos: los pesos de tf_idf.vector
            :se crea: una lista ordenada de el par de atributos (atributo y peso)
        """
        atributos = set()
        tfidf_score = dict([])
        # generate normal feature vector
        for articulo, documento_scores in pesos.iteritems():
            mas = dict(sorted(documento_scores.items(), key=itemgetter(1), reverse=True)[:5])
            for palabra, score in mas.items():
                if score > 0.0:
                    atributos.add(palabra)
                    tfidf_score[palabra] = score
        # reducir el vetor hasta un 10%
        longitud = len(atributos) / 10
        atributo_pareado = dict(sorted(tfidf_score.items(), key=itemgetter(1), reverse=True)[:longitud])
        self.atributos.append(sorted(atributos))
        util.guardar(os.getcwd()+"/preproceso/vocabulario.txt" ,self.atributos)
        self.atributos.append(sorted(atributo_pareado))

    def crear_dataset(self,pesos,documentos,atributos_doc):
        dataset = dict([])
        for i, documento in enumerate(documentos):
            dataset[i] = []
            for atributo in atributos_doc:
                dataset[i].vector.append(pesos[i][atributo])
        self.espacio_vectorial.append(dataset)


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

def crearListaTemasTotales(documentos):
    lista = set()
    lista.add("none")
    for doc in documentos:
        for tema in doc.temas:
            lista.add(tema)
    print(lista)
    return lista

def shuffle_split(directorio):
    documentos = escanear_docs(directorio)
    random.shuffle(documentos)
    train_data = documentos[:int((len(documentos)+1)*.80)]
    test_data = documentos[int(len(documentos)*.80+1):]
    return train_data, test_data

def preprocesar_train(directorio_ruta):
    #directorio = 'datos'
    print('\nGenerando los vectores de las instancias')
    train, test = shuffle_split(directorio_ruta)
    lista = list(crearListaTemasTotales(train) & crearListaTemasTotales(test))
    print(len(lista))
    for doc in train:
        doc.asignarTemaNumerico(lista)
    util.guardar(os.getcwd()+"/preproceso/lista_temas", lista)
    tfidf = Tf_Idf()
    tfidf.generar_vector_tupla_pesos(train)
    util.guardar(os.getcwd()+"/preproceso/lista_articulos_train", train)
    util.guardar(os.getcwd()+"/preproceso/lista_articulos_test", test)
    util.guardar(os.getcwd()+"/preproceso/train_tfidf", tfidf)
    print('Preproceso completado!')
    return tfidf, train

def preprocesar_test(tfidf, newData, vocabulario_path, lista_temas_path):
    #directorio = 'testing'
    print('\nGenerando los vectores de las instancias')
    n_docs = len(tfidf)
    n_new_inst = len(newData)
    lista = list(crearListaTemasTotales(newData) & util.cargar(lista_temas_path))
    util.guardar('new_lista_temas', lista)
    for doc in newData:
        doc.asignarTemaNumerico(lista)
    listaVocabulario = util.cargar(vocabulario_path)
    tfidf = tfidf.generar_vector_tupla_pesos_newInst(newData, listaVocabulario)
    print('Preproceso completado!')
    return tfidf, n_docs, n_new_inst