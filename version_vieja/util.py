# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:00:38 2019

@author: StromValhalla
"""
import pickle

"""
    Dado una lista de vectores te devuelve su centroide
    pre: Una lista no vacia de tuplas numericas
    post: Devuelve el centroide de esos vectores
"""
def calcularCentro(lista, vectores):
    centro = []
    i=0
    x=0
    
    while i<len(vectores[0]):
        for each in lista: 
            vector = vectores[each]
            x+=vector[i]
            
            
        x=x/len(lista)
        centro.append(x)
        x=0
        i+=1
    
    centro = tuple(centro)
    return centro


"""
    Se encarga de actualizar las lista con los clusters que se han asignado a cada instancia
    pre: una lista de vectores, las agrupaciones y una lista
    post: Devuelve la lista con la correspondiente agrupacion
"""
def listaClusters(inst, agrup, lista): 
    for clust in agrup.keys():
        for each in agrup[clust]:
            "indice = inst.index(each)"
            lista[each] = clust
            
            
    return lista



"""
Guarda la estructura de datos
Pre : El path debe existir
Post: El archivo con la estructura de datos guardada
"""
def guardar(path, archivo):
    with open(path, "wb") as res:
        pickle.dump(archivo, res)     
        
    res.close()


"""
Carga la estructura de datos
Pre : El path debe existir
Post: La estructura de datos
"""
def cargar(path):
    with open(path, "rb") as fp:  
        clust = pickle.load(fp)
        
    fp.close()

    return clust


"""
Genera una lista con ceros
Pre : La longitud de la lista
Post: U lista
"""
def generarLista(num):
    l = [0] * num
    return l