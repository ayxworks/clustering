# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
import util as ut
from copy import copy

class Cluster:
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = {}
        i = 0
        while i<len(vectores): 
            self.clust[i+1] = [i]
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
        centroides = self.inicializarCentroides()
        
        while len(self.clust.keys()) != 1:
            print(iteracion)
            
            print("Centroides calculados")
            cl1, cl2, dist = ut.minimaDistancia(centroides)
            print("Distancia calculada")
            
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            
            del self.clust[cl2]
            del centroides[cl2]
            
            self.clust[cl1] = vector1 + vector2
            "vectores = self.sacarVetores(self.clust[cl1], self.vect)"
            centroides[cl1] = ut.calcularCentro(self.clust[cl1], self.vect)
            
            self.dist[dist] = copy(self.clust)
            
            self.guardarIteracion(iteracion, dist, self.clust)
            
            iteracion+=1
            
        "print(self.dist)"
    
    
    def inicializarCentroides(self):
        centroides = {} 
        
        for each in self.clust.keys():
            "vectores = self.sacarVetores(self.clust[each], self.vect)"
            centroide = ut.calcularCentro(self.clust[each], self.vect)
            centroides[each] = centroide
            
        return centroides
    
    
    
    """def sacarVetores(self, lista, vect):
        vectores = []
        for num in lista:
            vectores.append(vect[num])
        
        return vectores"""
    
    
    def guardarIteracion(self, it, dist, clust):
        string = ' Iteration={};  '.format(it)
        string += 'Distancia={0:.2f};  '.format(round(dist, 2))
        for cl in clust.keys(): string += '{};  '.format(clust[cl])
        string += '\n' 
        with open('resultados\iteraciones.txt', "a") as res: res.write(string)
        
        res.close()
        
            

"""with open('resultados\datosAL.txt', "rb") as fp:  
    clust = pickle.load(fp)"""

cl = Cluster([(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)])
"cl = Cluster(clust)"

cl.clustering() 
print(cl.dist.keys())

ut.guardar('resultados\dist.txt', cl.dist)








