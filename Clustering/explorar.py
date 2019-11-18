# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:40:07 2019

@author: StromValhalla
"""

import util as ut


"""
Escribe en resultados\Asig.txt la asignacion de cada instancia segun la distancia dada
Pre : El path debe existir, las instancias y la distancia maxima
Post: resultados\Asig.txt con los resultados
"""
def clusterDist(path, instancias, dist):
    distancias = ut.cargar(path)
    nivel = 0
    
    for each in distancias.keys():
        if each<=dist and each>nivel: nivel = each
    
    clusters = distancias[nivel]
    lista = ut.generarLista(len(instancias))
    asig = ut.listaClusters(instancias, clusters, lista)
    i=0
    
    while i<len(instancias): 
        guardarAsig(instancias[i], asig[i])
        i+=1
    
    
"""
Escribe en resultados\Asig.txt la asignacion de cada instancia segun la distancia dada
Pre : la instancia y la asignacion
Post: una nueva linea en resultados\Asig.txt
"""
def guardarAsig(inst, asig):
    string = ' Cluster: {}  '.format(asig)
    string += 'Instancia: {}'.format(inst)
    string += '\n' 
    with open('resultados\Asig.txt', "a") as res: res.write(string)
    
    res.close()
    

  
"""
Devuelve los centroides segun el numero de agrupaciones
Pre : El path debe existir, las instancias y el numero de clusters
Post: Los centroides calculados
"""
def clustersIteracion(path, instancias, numclus):
    iteraciones = ut.cargar(path)
    clusters = iteraciones[len(instancias)-numclus]
    print(len(clusters))
    centroides = ut.generarLista(len(clusters))
    i = 0
    
    while i<len(clusters):
        centroide = ut.calcularCentro(clusters[i], instancias)
        centroides[i] = centroide
        i+=1
        
    return centroides

"""
Agrupa una lista de instancias a un numero elegido de clusters
Pre:El path debe existir, las instancias y el numero de clusters
Post: Lista de instancia, cluster al cual ha sido agrupado y la distancia a su centroide.
"""

def agruparInstanciasPorCluster(path,instancias,numClus,instsAClasif, vectoresTest, datosTest): #instAClasificar debera ser posicion o id
    #vectoresTest = ut.cargar('/preproceso/new_tfidf')
    #datosTest=ut.cargar('/preproceso/new_lista_articulos')
    centroides = clustersIteracion(path,instancias,numClus)
    agrupacion=[]
    cAct=0
    c=0;"Indice centroide"
    for inst in instsAClasif: #Recorrer instancias a clasificar
        vecInst=vectoresTest[inst] #Coger el vector de la instancia TODO
        mindist = 999999
        for cent in centroides: #Por cada centroide...
            distancia = ut.calcularDistancia(cent,vecInst,1) #Buscar menor distancia manhattan centroide e instancia
            if distancia<mindist:
                mindist=distancia
                centAct=cent
                cAct=c#Indice del centroide/cluster dentro de la lista de centroides/clusters
            c+=1

        iteraciones = ut.cargar(path)
        clusters = iteraciones[len(instancias) - numClus]; "Sabiendo la posicion se que cluster llevarme"
        tema= temaMasComunEnInstancia(clusters[cAct],vecInst); "Pasar instancias del cluster del cent, el id y vector de instAClasif"
        temaReal = datosTest.tema_numerico[inst]
        agrupacion.append((inst,cent,tema, temaReal)) #Instancia, centroide, tema agrupado, tema real


    return agrupacion

def temaMasComunEnInstancia(instCluster,vecInst): #instCluster son posiciones, instancia es vector
    "Recorrer instancias de cluster, coger las 10 mas cercanas a la instancia daba y devolver el maximo de los temas"
    i=1
    temas=[]
    vectoresTrain=ut.cargar('/preproceso/train_tfidf')
    datosTrain=ut.cargar('/preproceso/lista_articulos_train')
    j=0
    while j<121:
        temas= temas+[(j,0)] #(TemaNumerico,Contador)
    instancias=[] #Lista de 10 instancias mas cercanas a la instancia test
    distancias=[] #Lista de distancias de instancias cluster a instancia test

    for instCl in instCluster: #Instancias del cluster
        vecInstCl=vectoresTrain.vector[instCl]
        distancias.append(instCl,ut.calcularDistancia(vecInstCl,vecInst,2))#Coger la menor (Instancia cluster, distancia)
    while i>=10:
        actual = min(distancias, key = lambda t: t[1]) #Devuelve la tupla con la instancia del cluster y la distancia minima a la distancia a clasificar.
        distancias.remove(actual)
        instancias.append(actual[0])
        i+=1

    "Buscar tema mayor entre las 10 instancias y ese sera el de la instancia a clasificar."
    for posInst in instancias:
        indTema = datosTrain.tema_numerico[posInst]
        t=0
        while t<121:
            if t==indTema:
                temas[t][1]+=1
                t=121
            t+=1

    tema=max(temas,key = lambda t: t[1]) #Devuelve el tema que mas veces ha aparecido
    return tema[0]

    


"""clusterDist('resultados\dist.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 3)

print(clustersIteracion('resultados\iter.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 3))"""
"agruparInstanciasPorCluster('resultados\iteraciones.txt', [(1,3),(1,4),(2,2),(5,2),(5,1),(7,2)], 3,[(2,1),(3,1),(7,0)])"