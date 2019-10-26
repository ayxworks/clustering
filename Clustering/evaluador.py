# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:59:51 2019

@author: StromValhalla
"""
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
import util as ut

class Evaluador:
    
    def evaluar(self, path, instancias):
        res = ut.cargar(path)
        labels = ut.generarLista(len(instancias))
        i = 0

        for each in res.keys():
            if i != 0 and i != len(res.keys())-1:
                agrup = res[each]
                labels = ut.listaClusters(instancias, agrup, labels)
                score = self.calinskiHarabasz(instancias, labels)
                print('Agrupaciones: {}   Score: {}' .format(len(agrup.keys()), score))
            
            i+=1
            
        
        "Falta por implementar pero he estado probando cosas para ver si funcionaba"
        
        
        
    
    def daviesBouldin(self, inst, labels):
        score = davies_bouldin_score(inst, labels)
        return score
    
    
    
    def calinskiHarabasz(self, inst, labels):
        score = calinski_harabasz_score(inst, labels)
        return score
    
        

ev = Evaluador()
ev.evaluar('resultados\dist.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)])