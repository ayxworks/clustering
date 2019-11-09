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
        "parar = False"
        scoreMax = 0
        salto = math.ceil(len(res.keys())*0.01)

        for each in res.keys():
            "if i!=0 and i%10==0 and i <= hasta and not parar:"
            if i!=0 and i%salto==0 and i<len(res.keys())-1:
                agrup = res[each]
                labels = ut.listaClusters(instancias, agrup, labels)
                score = self.daviesBouldin(instancias, labels)
                self.guardarScore(len(agrup), score)
                if score>scoreMax: scoreMax = score
                """elif score<scoreMax: 
                    parar = True
                    print(score)"""
                
            i+=1
            
    
    """
        Calcula el indice externo de avaluacion Davies Bouldin
        Pre: La lista de vectores y sus asignaciones
        Post: El score equivalente a ese numero de agrupaciones
    """
    def daviesBouldin(self, inst, labels):
        score = davies_bouldin_score(inst, labels)
        return score
    
    
    
    def calinskiHarabasz(self, inst, labels):
        score = calinski_harabasz_score(inst, labels)
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
        

"""clust = ut.cargar('resultados\datosAL.txt')
ev = Evaluador()
ev.evaluar('resultados\dist.txt', clust)"""
