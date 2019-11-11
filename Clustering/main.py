import sys
import time
import preproceso
import util

def main(argv):
    comienzo = time.time()
    print('\n')
    ##########################################################################################
    print('1: Preprocessing')
    documentos, tfidf_vecs = preproceso.preprocesar_train()
    #util.guardar("/prueba_pickle", documentos)
    #prueba = util.cargar("/prueba_pickle")
    #print(documentos.vector)
    #print(documentos.atributos)
    #print(documentos.tabla)
    #documentos.print_tabla()
    print(tfidf_vecs.vDocs[0]) #lista de tuplas(/vectores)
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
if __name__ == '__main__':
    main(sys.argv[1:])

def readCommand( argv ):
    """
    Funcion que permite pasar argumentos en el terminal .
    """
    from optparse import OptionParser
    usageStr = """
    USO:      python main.py <options>
    EJEMPLOS:   (1) python main.py
                    - starts an interactive game
                (2) python main.py --layout smallClassic --zoom 2
                OR  python main.py -l smallClassic -z 2
                    - starts an interactive game on a smaller board, zoomed in
    """
    parser = OptionParser(usageStr)

    parser.add_option('-p', '--preproceso', dest='pacman',
                      help=default('the agent TYPE in the pacmanAgents module to use'),
                      metavar='TYPE', default='KeyboardAgent')
    parser.add_option('-t', '--textGraphics', action='store_true', dest='textGraphics',
                      help='Display output as text only', default=False)
    parser.add_option('-c', '--quietTextGraphics', action='store_true', dest='quietGraphics',
                      help='Generate minimal output and no graphics', default=False)
    parser.add_option('-g', '--ghosts', dest='ghost',
                      help=default('the ghost agent TYPE in the ghostAgents module to use'),
                      metavar = 'TYPE', default='RandomGhost')


    options, otros = parser.parse_args(argv)
    if len(otros) != 0:
        raise Exception('No se ha entendido este comando: ' + str(otros))
    args = dict()

    # Choose a layout
    args['layout'] = layout.getLayout( options.layout )
    if args['layout'] == None: raise Exception("The layout " + options.layout + " cannot be found")

    # Choose a Pacman agent
    noKeyboard = options.gameToReplay == None and (options.textGraphics or options.quietGraphics)
    pacmanType = loadAgent(options.pacman, noKeyboard)
    agentOpts = parseAgentArgs(options.agentArgs)
    if options.numTraining > 0:
        args['numTraining'] = options.numTraining
        if 'numTraining' not in agentOpts: agentOpts['numTraining'] = options.numTraining
    pacman = pacmanType(**agentOpts) # Instantiate Pacman with agentArgs
    args['pacman'] = pacman

    # Don't display training games
    if 'numTrain' in agentOpts:
        options.numQuiet = int(agentOpts['numTrain'])
        options.numIgnore = int(agentOpts['numTrain'])

    # Choose a ghost agent
    ghostType = loadAgent(options.ghost, noKeyboard)
    args['ghosts'] = [ghostType( i+1 ) for i in range( options.numGhosts )]

    # Choose a display format
    if options.quietGraphics:
        import textDisplay
        args['display'] = textDisplay.NullGraphics()
    elif options.textGraphics:
        import textDisplay
        textDisplay.SLEEP_TIME = options.frameTime
        args['display'] = textDisplay.PacmanGraphics()
    else:
        import graphicsDisplay
        args['display'] = graphicsDisplay.PacmanGraphics(options.zoom, frameTime = options.frameTime)
    args['numGames'] = options.numGames
    args['record'] = options.record
    args['catchExceptions'] = options.catchExceptions
    args['timeout'] = options.timeout

    return args