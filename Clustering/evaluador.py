# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:59:51 2019

@author: StromValhalla
"""
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import jaccard_score
import math
import util as ut
import explorar as ex

class Evaluador:
    
    """
        Evalua el clustering segun un indice de evaluacion externa
        Pre: El path donde se encuentra la estructura de datos con el clustering y la lista de vectores
        Post: Un archivo en resultados\score.txt donde se recopilan todos los resultados
    """
    def evaluar(self, path, instancias):
        res = ut.cargar(path)
        labels = ut.generarLista(len(instancias))
        i = 0
        scoreMax = 99999999999
        agrupF = 0
        salto = math.ceil(len(res.keys())*0.01)

        for each in res.keys():
            "if i!=0 and i%10==0 and i <= hasta and not parar:"
            if i!=0 and i%salto==0 and i<len(res.keys())-1:
                agrup = res[each]
                labels = ut.listaClusters(instancias, agrup, labels)
                score = self.daviesBouldin(instancias, labels)
                self.guardarScore(len(agrup), score)

                if score<scoreMax: 
                    scoreMax = score
                    agrupF = len(agrup)-(i+1)
                
            i+=1
        
        string = ' La mejor agrupacion es con {} '.format(agrupF)
        string += 'clusters con un score de {}'.format(round(scoreMax, 4))
        print(string)
            
    
    """
        Calcula el indice externo de avaluacion Davies Bouldin
        Pre: La lista de vectores y sus asignaciones
        Post: El score equivalente a ese numero de agrupaciones
    """
    def daviesBouldin(self, inst, labels):
        score = davies_bouldin_score(inst, labels)
        return score
    
    
    """
        Calcula el indice externo de avaluacion Calinski Harabasz
        Pre: La lista de vectores y sus asignaciones
        Post: El score equivalente a ese numero de agrupaciones
    """
    def calinskiHarabasz(self, inst, labels):
        score = calinski_harabasz_score(inst, labels)
        return score


    """
        Calcula el indice interno de avaluacion Jaccard Index
        Pre: La agrupacion
        Post: El score equivalente a la agrupacion
    """
    def jaccard(self, agrupacion):
        temasR=[]
        temasY=[]
        for each in agrupacion:
            temasY.append(each[2])
            temasR.append(each[3])
        score = jaccard_score(temasR,temasY)
        "print (score)"
        return score
    
    
    """
        Guarda los resultados en resultados\score.txt
        Pre: El numero de agrupaciones y su score
        Post: El archivo resultados\score.txt
    """
    def guardarScore(self, num, score):
        string = ' Agrupaciones: {}   '.format(num)
        string += 'Score: {}'.format(round(score, 4))
        string += '\n' 
        with open('resultados\score.txt', "a") as res: res.write(string)
        
        res.close()
        

"clust = ut.cargar('resultados\datosAL.txt')"
"""clust = [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)]
ev = Evaluador()
ev.evaluar('resultados\dist.txt', clust)"""

path='resultados\iteraciones.txt'
instancias = 0 #TODO Vectores de todas las instancias
numClus=3
instsAClasif = 0 #TODO Posiciones de todas las nuevas instancias a clasificar
agrupacion = ex.agruparInstanciasPorCluster(path,instancias,numClus,instsAClasif)
for each in agrupacion:
    print (each[2],each[3])
ev = Evaluador()
jaccardScore = ev.jaccard(agrupacion)