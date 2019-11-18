Nota: para que funcione hace falta tener en el main comentado el import del evaluador,
ya que se ha dejado de forma automática e intenta cargar un archivo antes de haberse creado.
Intenta cargar test_tfidf pero este solo se genera tras la ejecucion del preproceso y separacion de train y test

Para ejecutar el preproceso 
python main.py -r

Para ejecutar el clustering
python main.py -s

para ejecutar la evaluación del cluster NOTA: la evaluacion se ha omitido del main ya que daba problemas en la memoria y no se han podido realizar
python main.py t

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
  -p PREPROCESO, --preproceso=PREPROCESO
                        Se hace el preproceso de textos
  -c CREAR_CLUSTER, --crear_cluster=CREAR_CLUSTER
                        Se crea el cluster y se calculan las distancias
  -z TESTING, --testing=TESTING
                        Pruebas
  -r, --skip_preproceso
                        Flag para saltarse el preproceso
  -s, --skip_clustering
                        Flag para saltarse el clustering
  -t, --skip_evaluacion
                        Flag para saltarse la evaluacion
  -u, --skip_newInst    Flag para saltarse el apartado de anadir nuevas
                        instancias
  -a ASIGNAR_CLUSTER, --asignar_cluster=ASIGNAR_CLUSTER
                        Elegir un cluster si ya hay una estructura
  -e EVALUATION, --evaluation=EVALUATION
                        Se hace la evaluacion del cluster
  -n NEWINST, --newInst=NEWINST
                        Para añadir nuevas instancias al cluster
  -d DISTANCIA, --distancia=DISTANCIA
                        Elegir la ecuación para las distancias 1=manhattan,
                        2=euclidea (predeterminado)