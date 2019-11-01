# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:40:07 2019

@author: StromValhalla
"""

import util as ut


"""
Escribe en un .txt la asignacion de cada instancia segun la distancia dada
Pre : El path debe existir, las instancias y la distancia maxima
Post: resultados\Asig.txt con los resultados
"""
def clusterDist(path, instancias, dist):
    distancias = ut.cargar(path)
    nivel = 0
    
    for each in distancias.keys():
        if each<=dist and each>nivel: nivel = each
    
    clusters = distancias[nivel]
    lista = ut.generarLista(len(instancias))
    asig = ut.listaClusters(instancias, clusters, lista)
    i=0
    
    while i<len(instancias): 
        guardarAsig(instancias[i], asig[i])
        i+=1
    
    
"""
Escribe en resultados\Asig.txt la asignacion de cada instancia segun la distancia dada
Pre : la instancia y la asignacion
Post: una nueva linea en resultados\Asig.txt
"""
def guardarAsig(inst, asig):
    string = ' Cluster: {}  '.format(asig)
    string += 'Instancia: {}'.format(inst)
    string += '\n' 
    with open('resultados\Asig.txt', "a") as res: res.write(string)
    
    res.close()
    

  
"""
Devuelve los centroides segun el numero de agrupaciones
Pre : El path debe existir, las instancias y el numero de clusters
Post: Los centroides calculados
"""
def clustersIteracion(path, instancias, numclus):
    iteraciones = ut.cargar(path)
    clusters = iteraciones[len(instancias)-numclus]
    print(len(clusters))
    centroides = ut.generarLista(len(clusters))
    i = 0
    
    while i<len(clusters):
        centroide = ut.calcularCentro(clusters[i], instancias)
        centroides[i] = centroide
        i+=1
        
    return centroides
    
    
    


clusterDist('resultados\dist.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 3)

print(clustersIteracion('resultados\iter.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 3))