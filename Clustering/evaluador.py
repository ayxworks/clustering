# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:59:51 2019

@author: StromValhalla
"""
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
import util as ut
import pickle

class Evaluador:
    
    def evaluar(self, path, instancias, dist):
        res = self.cargar(path)
        labels = ut.generarLista(len(instancias))
        i = 0

        for each in res.keys():
            if i != 0 and i != len(res.keys())-1:
                agrup = res[each]
                labels = self.listaClusters(instancias, agrup, labels)
                sil = self.calinskiHarabasz(instancias, labels)
                print('Agrupaciones: {}   Score: {}' .format(len(agrup.keys()), sil))
            
            i+=1
            
        
        "Falta por implementar pero he estado probando cosas para ver si funcionaba"
        
        


    def listaClusters(self, inst, agrup, lista):  
        for clust in agrup.keys():
            for each in agrup[clust]:
                "indice = inst.index(each)"
                lista[each] = clust
                
                
        return lista
        
        
    
    def daviesBouldin(self, inst, labels):
        score = davies_bouldin_score(inst, labels)
        return score
    
    
    
    def calinskiHarabasz(self, inst, labels):
        score = calinski_harabasz_score(inst, labels)
        return score
    
    
    
    def cargar(self, path):
        with open(path, "rb") as fp:  
            clust = pickle.load(fp)
            
        fp.close()
    
        return clust
        

ev = Evaluador()
ev.evaluar('resultados\dist.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 'manhattan')