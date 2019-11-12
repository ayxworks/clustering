import sys
import time
import preproceso
import util, clustering, evaluador

def runClusteringPruebas(argumentos):
    import __main__
    comienzo = time.time()
    print('\n')
    ##########################################################################################
    print('1: Preprocessing')
    #directorio_ruta = 'datos'
    print(argumentos)
    documentos, tfidf_vecs = preproceso.preprocesar_train(argumentos.preproceso)
    #prueba = util.cargar("/prueba_pickle")
    #print(documentos.vector)
    #print(documentos.atributos)
    #print(documentos.tabla)
    #documentos.print_tabla()
    #print(tfidf_vecs.vDocs[0]) #lista de tuplas(/vectores)
    #print(prueba.vDocs[0]) 

    tiempo = time.time() - comienzo
    tiempo = time.strftime("%H:%M:%S", time.gmtime(tiempo))
    print ('Ha tardado en preprocesar ', tiempo, 'segundos!')
    ##########################################################################################
    print('2: Clustering')
    #clustering.begin(fv)

    tiempo = time.time() - comienzo
    tiempo = time.strftime("%H:%M:%S", time.gmtime(tiempo))
    print ('Ha tardado en hacer el cluster jerarquico ', tiempo, 'segundos!')
    ##########################################################################################


    tiempo = time.time() - comienzo
    tiempo = time.strftime("%H:%M:%S", time.gmtime(tiempo))
    print ('Ha tardado en evaluar ', tiempo, 'segundos!')

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
    """
    parser = OptionParser(usageStr)
    parser.add_option('-p', '--preproceso', dest='preproceso',
                      help='Se hace el preproceso de textos', default='datos')
    parser.add_option('-c', '--crear_cluster', action='store', dest='crear_cluster',
                      help='Se crea el cluster y se calculan las distancias', default='train_tfidf')
    parser.add_option('-t', '--testing', action='store', dest='testing',
                      help='Pruebas', default='lista_articulos_test')
    parser.add_option('-r','--skip_preproceso', action='store_true', dest='skip_preproceso',
                      help='Flag para saltarse el preproceso', default=True)
    parser.add_option('-s', '--skip_clustering', action='store_true', dest='skip_clustering',
                      help='Flag para saltarse el clustering', default=True)
    parser.add_option('-a', '--asignar_cluster', dest='asignar_cluster',
                      help='Elegir un cluster si ya hay una estructura', default='resultados\datosAL.txt')
    parser.add_option('-e', '--evaluation', dest='evaluation',
                      help='Se hace la evaluacion del cluster', default='resultados\dist.txt')
    parser.add_option('-n', '--newInst', action='store', dest='newInst',
                      help='Para añadir nuevas instancias al cluster', default='test\new')
    parser.add_option('-d', '--distancia', action='store', dest='distancia',
                      help='Elegir la ecuación para las distancias 1=manhattan predeterminado', type="int", default=1)

    options, otros = parser.parse_args(argv)
    if len(otros) != 0:
        raise Exception('No se ha entendido este comando: ' + str(otros))
    return options

if __name__ == '__main__':
    print('start')
    args = readCommand( sys.argv[1:] )
    runClusteringPruebas(args)
    pass