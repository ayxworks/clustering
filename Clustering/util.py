# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:00:38 2019

@author: StromValhalla
"""

def minimaDistancia (centroides):
    distMin = 99999
    i = 1
    j=0
    solucion=()

    for cent1 in centroides.keys():
        if i==len(centroides):
            "print(solucion)"
            return solucion
        else:
            for cent2 in centroides.keys():
                if j>0:
                    if cent1 != cent2:
                        distAct = distManhattan(centroides[cent1],centroides[cent2])
                        if distAct<distMin:
                            distMin=distAct
                            solucion = (cent1,cent2,distMin)
                j+=1
            i+=1

"""
    Calcula la distancia manhattan entre dos centroides.
    Pre : Coordenadas de dos centroides
    Post: Distancia Manhattan entre los dos centroides.
"""
def distManhattan(centr1, centr2):
    dist=0
    i=0
    while i<len(centr1):
        dist+= abs(centr1[i]-centr2[i])
        i+=1
    return dist


"""
    Dado una lista de vectores te devuelve su centroide
    pre: Una lista no vacia de tuplas numericas
    post: Devuelve el centroide de esos vectores
"""
def calcularCentro (lista):
    centro = []
    i=0
    x=0
    
    while i<len(lista[0]):
        for each in lista: x+=each[i]
        x=x/len(lista)
        centro.append(x)
        x=0
        i+=1
    
    centro = tuple(centro)
    return centro