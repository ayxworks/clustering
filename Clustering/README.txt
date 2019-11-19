Para ejecutar el preproceso hace falta tener las instancias en una carpeta datos y tener una carpeta preproceso creada
python3 main.py -r

Para ejecutar el clustering hace falta tener una carpeta resultados
python3 main.py -s

para ejecutar la evaluación del cluster
python3 main.py -t

para agrupar instancias al cluster mas cercano y devolver el tema estimado, para evaluar nuevas instancias, tienen que estar metidas en la carpeta test
python3 main.py-u


Ejemplos de uso
    USO:      python main.py <opciones>
    EJEMPLOS:   (1) python main.py
                    - Se hace el preproceso y el cluster en carpetas predeterminadas
                (2) python main.py --preproceso carpeta_preproceso --clustering carpeta_cluster
                OR  python main.py -l carpeta_preproceso -z carpeta_cluster
                    - Se hace el preproceso y el cluster en carpetas predeterminadas

            Para mas informacion utilizar -h o --help
                python main.py -h


Opciones:
  -h, --help            show this help message and exit
  -z TESTING, --testing=TESTING
                        Pruebas
  -g, --get_instance    Coge la instancia del indice seleccionado e imprime
                        por pantalla
  -j, --get_temas       Coge los temas procesados e imprime por pantalla
  -i INDICE_INSTANCIA, --indice_instancia=INDICE_INSTANCIA
                        Se elige el indice de una instancia
  -r, --skip_preproceso
                        Flag para saltarse el preproceso
  -s, --skip_clustering
                        Flag para saltarse el clustering
  -t, --skip_evaluacion
                        Flag para saltarse la evaluacion
  -u, --skip_newInst    Flag para saltarse el apartado de anadir nuevas
                        instancias
  -w, --skip_test       Flag para saltarse el apartado de anadir instancias
                        del test que no estan en el cluster
  -a ASIGNAR_CLUSTER, --asignar_cluster=ASIGNAR_CLUSTER
                        Elegir un cluster si ya hay una estructura
  -e EVALUACION, --evaluacion=EVALUACION
                        Se hace la evaluacion del cluster
  -y ITERACIONES, --iteraciones=ITERACIONES
                        Path de las iteraciones del cluster
  -b BACKUP_DATOS, --backup_datos=BACKUP_DATOS
                        Path del archivo donde se guardan las instancias
  -v BACKUP_DATOS_TEST, --backup_datos_test=BACKUP_DATOS_TEST
                        Path del archivo donde se guardan las instancias para
                        test
  -p PREPROCESO, --preproceso=PREPROCESO
                        Path de los textos
  -c VECTOR_TUPLA, --vector_tupla=VECTOR_TUPLA
                        Path de los vectores para hacer el cluster
  -n NEWINST, --newInst=NEWINST
                        Para añadir nuevas instancias al cluster
  -d DISTANCIA, --distancia=DISTANCIA
                        Elegir la ecuación para las distancias 1=manhattan,
                        2=euclidea (predeterminado)

