# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
import util as ut
from copy import copy
import distancias as dis

class Cluster:

    """
        Se encarga de inicializar la clase dado la lista de vectores
        Pre: una lista de tuplas numericas con el mismo espacio vectorial
        Post: Nada
    """
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = ut.generarLista(len(vectores))
        i = 0
        while i<len(vectores): 
            self.clust[i] = [i]
            i+=1
        
        self.dist = {}
        self.dist[0] = copy(self.clust)
        self.iter = ut.generarLista(len(vectores))
        self.iter[0] = copy(self.clust)



    """
    Hace el poceso de clustering
    Pre : Haber creado la clase con los vectores numericos, y pasar el coeficiente para el calculo de distancias.
    Post: La estructura jerarquica de la agrupacion
    """
    def clustering (self, dist):
        iteracion = 1
        centroides = self.inicializarCentroides()
        print('Centroides calculados')
        distancias = dis.Distancias(len(self.vect), dist)
        distancias.inicializarDist(centroides)
        print('Distancias calculada')
        
        while len(self.clust) != 1:
            print(iteracion)
            
            cl1, cl2, dist = distancias.minimaDist()
            
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            self.clust[cl1] = vector1 + vector2
            centroides[cl1] = ut.calcularCentro(self.clust[cl1], self.vect)
            
            distancias.actualizarDist(centroides, cl1, cl2)
            
            del self.clust[cl2]
            del centroides[cl2]
            
            
            self.dist[dist] = copy(self.clust)
            self.iter[iteracion] = copy(self.clust)
            
            self.guardarIteracion(iteracion, dist, self.clust)
            
            iteracion+=1
            
        ut.guardar('resultados\dist.txt', self.dist)
        ut.guardar('resultados\iter.txt', self.iter)
    
    
    """
    Inicializa los clusters
    Pre : Que la clase tenga una lista de instancias
    Post: Devuelve una lista de centroides
    """
    def inicializarCentroides(self):
        centroides = ut.generarLista(len(self.clust))
        i=0
        
        while i < len(self.clust):
            centroide = ut.calcularCentro(self.clust[i], self.vect)
            centroides[i] = centroide
            i+=1
            
        return centroides
    
    
    """
    Guarda la informacion respecto a cada iteracion
    Pre : Un integer de la iteracion, la distancia calculada en la iteracion y los clusters
    Post: escribe la linea correspondiente con la informacion dada
    """
    def guardarIteracion(self, it, dist, clust):
        string = ' Iteration={};  '.format(it)
        string += 'Distancia={0:.2f};  '.format(round(dist, 2))
        for cl in clust: string += '{}; '.format(cl)
        string += '\n' 
        with open('resultados\iteraciones.txt', "a") as res: res.write(string)
        
        res.close()
        
            

"""clust = ut.cargar('resultados\datosAL.txt')

cl = Cluster(clust)"""
cl = Cluster([(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)])

cl.clustering(1)








