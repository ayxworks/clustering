import sys
import time
import preproceso

def main(argv):
    comienzo = time.time()
    print('\n')
    ##########################################################################################
    print('1: Preprocessing')
    documentos = preproceso.preprocesar()
    #print(documentos.vector)
    #print(documentos.atributos)
    #print(documentos.tabla)
    #documentos.print_tabla()
    print(documentos.vDocs[0]) #lista de tuplas(/vectores)

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
if __name__ == '__main__':
    main(sys.argv[1:])