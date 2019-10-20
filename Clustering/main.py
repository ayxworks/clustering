import sys
import time
import preproceso

def main(argv):
    comienzo = time.time()
    print('1: Preprocessing')
    documentos = preproceso.preprocesar()

    print('1.2: TF-IDF')
    claseTFIDF = preproceso.Tf_Idf()
    claseTFIDF.vector = preproceso.Tf_Idf.generar_TF_IDF(claseTFIDF, documentos)

    print('\nStep 3: Clustering')
    #clustering.begin(fv)

    tiempo = time.time() - comienzo
    print ('\nHa tardado', tiempo, 'segundos!')

if __name__ == '__main__':
    main(sys.argv[1:])