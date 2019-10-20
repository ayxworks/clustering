import sys
import time
import preproceso

def main(argv):
    comienzo = time.time()
    print('1: Preprocessing')
    documentos = preproceso.preprocesar()
    print (documentos)

    print('2: Clustering')
    #clustering.begin(fv)

    tiempo = time.time() - comienzo
    print ('Ha tardado', tiempo, 'segundos!')

if __name__ == '__main__':
    main(sys.argv[1:])