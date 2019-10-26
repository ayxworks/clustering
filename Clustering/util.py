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



def listaClusters(inst, agrup, lista):  
    for clust in agrup.keys():
        for each in agrup[clust]:
            "indice = inst.index(each)"
            lista[each] = clust
            
            
    return lista



"""
Guarda la estructura jerarquica
Pre : El path debe existir
Post: El archivo con la estructura de datos guardada
"""
def guardar(path, archivo):
    with open(path, "wb") as res:
        pickle.dump(archivo, res)     
        
    res.close()



def cargar(path):
    with open(path, "rb") as fp:  
        clust = pickle.load(fp)
        
    fp.close()

    return clust



def generarLista(num):
    l = [0] * num
    return l