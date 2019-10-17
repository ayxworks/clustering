# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:33 2019

@author: StromValhalla
"""
"""from numpy import mean"""

class Cluster:
    def __init__(self, vectores):
        self.vect = vectores
        self.clust = {}
        i = 1
        while i<len(vectores): 
            self.clust[f'C{i}'] = [vectores[i-1]]
            i+=1
        
        self.dist = {}
        self.dist[0] = self.clust

    
    def clustering (self):
        iteracion = 0
        
        while len(self.clust.keys()) != 1:
            centroides = {} 
            
            for each in self.clust.keys():
                print(self.clust[each])
                centroide = self.calcularCentro(self.clust[each])
                centroides[each] = centroide
                
            """Esta parte la tengo que cambiar, es solo provisional"""
            cl1, cl2, dist = ('C1', 'C2', 1.7)
    
            vector1 = self.clust[cl1]
            vector2 = self.clust[cl2]
            
            del self.clust[cl1]
            del self.clust[cl2]
            
            self.clust[cl1] = vector1 + vector2
            
            self.dist[dist] = self.clust
            iteracion+=1
            
            print(self.dist)


    def minimaDistancia (self, centroides):
        distMin = 99999
        i = 1
        j=0
        long = len(centroides)
        solucion=()

        while j<long-1:
            while i<long:
                distAct = self.distManhattan(centroides[j][1],centroides[i][1])
                if distAct<distMin:
                    distMin=distAct
                    solucion = (centroides[j][0],centroides[i][0],distMin)
                i+=1
            j+=1
            i=j+1
        print(solucion)
        return solucion

    """
        Calcula la distancia manhattan entre dos centroides.
        Pre : Coordenadas de dos centroides
        Post: Distancia Manhattan entre los dos centroides.
    """
    def distManhattan(self,centr1,centr2):
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
    def calcularCentro (self, lista):
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
    
    
    
    """Hacerlo manual? (Duda)"""
    """def calcularCentro (self, lista):
        lista = tuple(lista)
        centroide = tuple(mean(lista, axis=0))
        
        return centroide"""
        


cl = Cluster([(1,2),(3,5),(1,3),(8,5)])
centroides = [('C1',(3,7)),('C2',(2,2)),('C3',(9,1)),('C4',(4,6))]

cl.minimaDistancia(centroides)