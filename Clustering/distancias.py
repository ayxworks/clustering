# -*- coding: utf-8 -*-
import util as ut
from copy import copy

class Distancias:

    """
        Se encarga de inicializar la matriz de distancias con valor cero
        Pre: El numero de instancias y el coeficiente para calcular las distancias
        Post: Nada
    """
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
                    distAct = ut.calcularDistancia(centroides[i],centroides[j],self.coeficiente)
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
                    self.dist[i][actualizar] = ut.calcularDistancia(centroides[i],centroides[actualizar], self.coeficiente)
                else:
                    self.dist[actualizar][i] = ut.calcularDistancia(centroides[i],centroides[actualizar],self.coeficiente)
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




