# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
from numpy import mean

class Cluster:
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = {}
        i = 1
        while i<len(self.vect): self.clust[i] = self.vect[i-1]

    
    def clustering (self):
        centroides = {} 
        
        for each in self.clust.keys():
            centroide = self.calcularCentro(self.clust[each])
            centroides[each] = centroide
            
        print(centroides)
        
    
    
    
    def calcularCentro (self, lista):
        lista = tuple(lista)
        centroide = tuple(mean(lista, axis=0))
        
        return centroide