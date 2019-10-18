# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
"""from numpy import mean"""
import util as ut
from copy import copy

class Cluster:
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = {}
        i = 1
        while i<len(vectores): 
            self.clust[f'C{i}'] = [vectores[i-1]]
            i+=1
        
        self.dist = {}
        self.dist[0] = copy(self.clust)

    
    def clustering (self):
        iteracion = 0
        
        while len(self.clust.keys()) != 1:
            centroides = {} 
            
            for each in self.clust.keys():
                centroide = ut.calcularCentro(self.clust[each])
                centroides[each] = centroide
                
            """Esta parte la tengo que cambiar, es solo provisional"""
            cl1, cl2, dist = ut.minimaDistancia(centroides)
    
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            del self.clust[cl2]
            
            self.clust[cl1] = vector1 + vector2
            
            self.dist[dist] = copy(self.clust)
            
            iteracion+=1
            
        print(self.dist)



        


cl = Cluster([(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)])
cl.clustering()



