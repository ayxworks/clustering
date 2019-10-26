# -*- coding: utf-8 -*-

class Distancias:
    def __init__(self):
        self.dist = {}

    """
        Dada una lista de centroides, inicializa el diccionario con las distancias entre centroides.
        Pre: Lista con los centroides de todos los clusters antes de realizar el clustering
        Post: Diccionario de distancias entre clusters inicializado.
    """
    def inicializarDist(self,centroides):
        distMin = 99999
        i = 1
        j=0
        solucion=()

        for cent1 in centroides.keys():
            if i==len(centroides):
                return solucion
            else:
                for cent2 in centroides.keys():
                    if j==i:
                        distAct = self.distManhattan(centroides[cent1],centroides[cent2])
                        self.dist[(cent1,cent2)]=distAct
                        if distAct<distMin:
                            distMin=distAct
                            solucion = (cent1,cent2,distMin)

                    else: j+=1

                i+=1
                j=0


    """
        Dada una lista de centroides, el cluster a actualizar y el cluster a eliminar, actualiza el diccionario de distancias tras unir dos clusters.
        Pre: Lista con los centroides, la key del cluster a actualizar y la key del cluster a eliminar.
        Post: Diccionario de distancias entre clusters actualizado.
    """
    def actualizarDist(self, centroides, actualizar, borrar):
        del self.dist[(actualizar,borrar)]

        for cent1 in centroides.keys():
            if cent1 != actualizar and cent1 != borrar:
                if cent1<actualizar:
                    
                    self.dist[(cent1,actualizar)] = self.distManhattan(centroides[cent1],centroides[actualizar])
                else:
                    self.dist[(actualizar,cent1)] = self.distManhattan(centroides[cent1],centroides[actualizar])

                if cent1<borrar:
                    del self.dist[cent1,borrar]
                else:
                    del self.dist[borrar,cent1]

    """
        Recorre el diccionario de distancias buscando la menor.
    """
    def minimaDist(self):
        minima=999999
        x = 0
        y = 0
        
        for i in self.dist.keys():
            act = self.dist[i]
            if act<minima:
                minima=act
                x, y = i

        
        return (x, y , minima)



    """
        Calcula la distancia manhattan entre dos centroides.
        Pre : Coordenadas de dos centroides
        Post: Distancia Manhattan entre los dos centroides.
    """
    def distManhattan(self, centr1, centr2):
        dist=0
        i=0
        while i<len(centr1):
            dist+= abs(centr1[i]-centr2[i])
            i+=1
            
        return dist
