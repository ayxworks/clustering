# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
import util as ut
from copy import copy
import distancias as dis

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
        print("Centroides calculados")
        distancias = dis.Distancias()
        distancias.inicializarDist(centroides)
        print("Distancias calculada")
        
        while len(self.clust.keys()) != 1:
            print(iteracion)
            
            print(centroides)
            cl1, cl2, dist = distancias.minimaDist()
            
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            
            del self.clust[cl2]
            del centroides[cl2]
            
            self.clust[cl1] = vector1 + vector2
            "vectores = self.sacarVetores(self.clust[cl1], self.vect)"
            centroides[cl1] = ut.calcularCentro(self.clust[cl1], self.vect)
            
            distancias.actualizarDist(centroides, cl1, cl2)
            
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
    
    
    
    def guardarIteracion(self, it, dist, clust):
        string = ' Iteration={};  '.format(it)
        string += 'Distancia={0:.2f};  '.format(round(dist, 2))
        for cl in clust.keys(): string += '{}; '.format(clust[cl])
        string += '\n' 
        with open('resultados\iteraciones.txt', "a") as res: res.write(string)
        
        res.close()
        
            


"clust = ut.cargar('resultados\datosAL.txt')"


cl = Cluster([(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)])
"cl = Cluster(clust)"

cl.clustering() 
print(cl.dist.keys())

ut.guardar('resultados\dist.txt', cl.dist)








