# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:59:51 2019

@author: StromValhalla
"""
from sklearn.metrics import silhouette_score
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
                sil = self.silhouette(instancias, labels, dist)
                print('Agrupaciones: {}   Silhouette: {}' .format(len(agrup.keys()), sil))
            
            i+=1
            
        
        "Falta por implementar pero he estado probando cosas para ver si funcionaba"
        
        


    def listaClusters(self, inst, agrup, lista):  
        for clust in agrup.keys():
            for each in agrup[clust]:
                indice = inst.index(each)
                lista[indice] = clust
                
                
        return lista
        
        
    
    def silhouette(self, inst, labels, metric):
        silhouette_avg = silhouette_score(inst, labels, metric=metric)
        return silhouette_avg
    
    
    
    def cargar(self, path):
        with open(path, "rb") as fp:  
            clust = pickle.load(fp)
    
        return clust
        

ev = Evaluador()
ev.evaluar('resultados\dist.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 'manhattan')