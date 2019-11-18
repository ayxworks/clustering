import os
import sys
import time
import preproceso
import util, clustering#, evaluador

def runClusteringPruebas(argumentos):
    import __main__
    comienzo = time.time()
    print('\n')
    ##########################################################################################
    if not argumentos.skip_preproceso:
        print('1: Preprocessing')
        #directorio_ruta = 'datos'
        print(argumentos)
        tfidf_vecs, documentos = preproceso.preprocesar_train(argumentos.preproceso)

        print ('Ha tardado en preprocesar ', calc_tiempo(comienzo), 'segundos!')
    ##########################################################################################
    if not argumentos.skip_clustering:
        print('2: Clustering')
        vector_dataset = util.cargar(os.getcwd() + argumentos.crear_cluster)
        print('Se ha cargado los vectores tf-idf, del directorio: ' + argumentos.crear_cluster)
        cl = clustering.Cluster(vector_dataset)
        cl.clustering(argumentos.distancia)
        print ('Ha tardado en hacer el cluster jerarquico ', calc_tiempo(comienzo), 'segundos!')
    ##########################################################################################
    if not argumentos.skip_evaluacion:
        print('3: Evaluando')

        print ('Ha tardado en evaluar ', calc_tiempo(comienzo), 'segundos!')    
    
    ##########################################################################################
    if not argumentos.skip_newInst:
        print('4: Anadir nuebba instancia')
        vector_dataset, ndocs, nNew = preproceso.preprocesar_test(argumentos.crear_cluster, "/preproceso/lista_articulos_train.txt", argumentos.newInst, "/preproceso/vocabulario.txt", "/preproceso/lista_temas.txt"):
        cl = clustering.Cluster(vector_dataset)
        cl.clustering(argumentos.distancia)
        print ('Ha tardado en anadir una nueva instancia ', calc_tiempo(comienzo), 'segundos!')
    
    print ('Fin del programa: ', calc_tiempo(comienzo), 'segundos!')
    print("Gracias por utilizar nuestro programa")

def readCommand( argv ):
    """
    Funcion que permite pasar argumentos en el terminal .
    """
    from optparse import OptionParser
    usageStr = """
    USO:      python main.py <options>
    EJEMPLOS:   (1) python main.py
                    - Se hace el preproceso y el cluster en carpetas predeterminadas
                (2) python main.py --preproceso carpeta_preproceso --clustering carpeta_cluster
                OR  python main.py -l carpeta_preproceso -z carpeta_cluster
                    - Se hace el preproceso y el cluster en carpetas predeterminadas
                    
            Para mas informacion utilizar -h o --help
                python main.py -h
    """
    parser = OptionParser(usageStr)
    parser.add_option('-p', '--preproceso', dest='preproceso',
                      help='Se hace el preproceso de textos', default='datos')
    parser.add_option('-c', '--crear_cluster', action='store', dest='crear_cluster',
                      help='Se crea el cluster y se calculan las distancias', default='/preproceso/train_tfidf')
    parser.add_option('-z', '--testing', action='store', dest='testing',
                      help='Pruebas', default='lista_articulos_test')
    parser.add_option('-r','--skip_preproceso', action='store_false', dest='skip_preproceso',
                      help='Flag para saltarse el preproceso', default=True)
    parser.add_option('-s', '--skip_clustering', action='store_false', dest='skip_clustering',
                      help='Flag para saltarse el clustering', default=True)
    parser.add_option('-t', '--skip_evaluacion', action='store_false', dest='skip_evaluacion',
                      help='Flag para saltarse la evaluacion', default=True)
    parser.add_option('-u', '--skip_newInst', action='store_false', dest='skip_newInst',
                      help='Flag para saltarse el apartado de anadir nuevas instancias', default=True)
    parser.add_option('-a', '--asignar_cluster', dest='asignar_cluster',
                      help='Elegir un cluster si ya hay una estructura', default='/resultados/datosAL.txt')
    parser.add_option('-e', '--evaluation', dest='evaluation',
                      help='Se hace la evaluacion del cluster', default='/resultados/dist.txt')
    parser.add_option('-n', '--newInst', action='store', dest='newInst',
                      help='Para añadir nuevas instancias al cluster', default='/test/new')
    parser.add_option('-d', '--distancia', action='store', dest='distancia',
                      help='Elegir la ecuación para las distancias 1=manhattan, 2=euclidea (predeterminado)', type="int", default=2)

    options, otros = parser.parse_args(argv)
    if len(otros) != 0:
        raise Exception('No se ha entendido este comando: ' + str(otros))
    return options
def calc_tiempo(comienzo):
    tiempo = time.time() - comienzo
    tiempo = time.strftime("%H:%M:%S", time.gmtime(tiempo))
    return tiempo

if __name__ == '__main__':
    print('start')
    args = readCommand( sys.argv[1:] )
    runClusteringPruebas(args)
    pass