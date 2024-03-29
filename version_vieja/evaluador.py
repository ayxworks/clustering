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
        parar = False
        scoreMax = 0
        hasta = len(res.keys())*0.9

        for each in res.keys():
            if i!=0 and i%10==0 and i <= hasta and not parar:
                agrup = res[each]
                labels = ut.listaClusters(instancias, agrup, labels)
                score = self.daviesBouldin(instancias, labels)
                self.guardarScore(len(agrup.keys()), score)
                if score>scoreMax: scoreMax = score
                elif score<scoreMax: 
                    parar = True
                    print(score)
                
            i+=1
            
        
        
        
    
    def daviesBouldin(self, inst, labels):
        score = davies_bouldin_score(inst, labels)
        return score
    
    
    
    def calinskiHarabasz(self, inst, labels):
        score = calinski_harabasz_score(inst, labels)
        return score
    
    
    def guardarScore(self, num, score):
        string = ' Agrupaciones: {}   '.format(num)
        string += 'Score: {}'.format(round(score, 4))
        string += '\n' 
        with open('resultados\score.txt', "a") as res: res.write(string)
        
        res.close()
        

clust = ut.cargar('resultados\datosAL.txt')
ev = Evaluador()
ev.evaluar('resultados\dist.txt', clust)