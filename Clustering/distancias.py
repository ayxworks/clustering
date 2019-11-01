# -*- coding: utf-8 -*-
import util as ut
from copy import copy

class Distancias:
    def __init__(self, num, m):
        lista = ut.generarLista(num)
        self.dist = [copy(lista) for i in range(num)]
        self.coeficiente = m

    """
        Dada una lista de centroides, inicializa el diccionario con las distancias entre centroides.
        Pre: Lista con los centroides de todos los clusters antes de realizar el clustering
        Post: Diccionario de distancias entre clusters inicializado.
    """
    def inicializarDist(self, centroides):
        i = 0
        j=1
        solucion=()

        while i < len(centroides)-1:
            if i+1==len(centroides):
                return solucion
            else:
                while j < len(centroides):
                    distAct = self.calcularDistancia(centroides[i],centroides[j],self.coeficiente)
                    self.dist[i][j] = distAct
                    j+=1

                i+=1
                j=i+1
        

    """
        Dada una lista de centroides, el cluster a actualizar y el cluster a eliminar, actualiza el diccionario de distancias tras unir dos clusters.
        Pre: Lista con los centroides, la key del cluster a actualizar y la key del cluster a eliminar.
        Post: Diccionario de distancias entre clusters actualizado.
    """
    def actualizarDist(self, centroides, actualizar, borrar):
        i=0
        while i < len(centroides):
            if i != actualizar and i != borrar:
                if i<actualizar:
                    self.dist[i][actualizar] = self.calcularDistancia(centroides[i],centroides[actualizar], self.coeficiente)
                else:
                    self.dist[actualizar][i] = self.calcularDistancia(centroides[i],centroides[actualizar],self.coeficiente)
            i+=1
            
            
        i=0
        while i < len(centroides):
            if i != borrar:
                del self.dist[i][borrar]
            i+=1
        
        del self.dist[borrar]
        

    """
        Recorre el diccionario de distancias buscando la menor.
    """
    def minimaDist(self):
        minima=999999
        x = 0
        y = 0
        i = 0
        j = 1
        
        while i < len(self.dist[0])-1:
            while j < len(self.dist[0]):
                act = self.dist[i][j]
                if act<minima:
                    minima=act
                    x, y = (i, j)
                j+=1
            
            i+=1
            j=i+1

        
        return (x, y , minima)



    """
        Calcula la distancia manhattan entre dos centroides.
        Pre : Coordenadas de dos centroides y valor m
            m=1 -> Distancia Manhattan
            m=2 -> Distancia Euclidea
            m=7.5 -> Distancia Minkowski
        Post: Distancia Manhattan, Euclidea o Minkowski entre los dos centroides.
    """
    def calcularDistancia(self, centr1, centr2, m):
        dist=0
        i=0
        while i<len(centr1):
            dist+= (abs(centr1[i]-centr2[i]))**m
            i+=1
        dist = dist**(1/m)
        return dist

