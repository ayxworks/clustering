# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
import util as ut
from copy import copy
import pickle

class Cluster:
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = {}
        i = 0
        while i<len(vectores): 
            self.clust[i+1] = [vectores[i]]
            i+=1
        
        self.dist = {}
        self.dist[0] = copy(self.clust)



    """
    Hace el poceso de clustering
    Pre : Haber creado la clase con los vectores numericos.
    Post: La estructura jerarquica de la agrupacion
    """
    def clustering (self):
        iteracion = 0
        
        while len(self.clust.keys()) != 1:
            centroides = {} 
            
            print(iteracion)
            
            for each in self.clust.keys():
                centroide = ut.calcularCentro(self.clust[each])
                centroides[each] = centroide
            
            print("Centroides calculados")
            cl1, cl2, dist = ut.minimaDistancia(centroides)
            
    
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            del self.clust[cl2]
            
            self.clust[cl1] = vector1 + vector2
            
            self.dist[dist] = copy(self.clust)
            
            iteracion+=1
            
        "print(self.dist)"
    
    
    
    """
    Guarda la estructura jerarquica
    Pre : El path debe existir
    Post: El archivo con la estructura de datos guardada
    """
    def guardar(self, path):
        with open(path, "wb") as res:   #Pickling
            pickle.dump(self.dist, res)


with open('resultados\datosAL.txt', "rb") as fp:  
    clust = pickle.load(fp)

cl = Cluster(clust)

cl.clustering() 
print(cl.dist.keys())

cl.guardar('resultados\dist.txt')








