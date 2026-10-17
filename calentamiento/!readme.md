en calentamiento_biblioteca.py están todas las funciones que se usan para el resto de cosas, si chequean todas son bastante intuitivas e intenté que los nombres describieran que hacen

las mas importantes son

sincronizar_grafo(G, tita0,titulo):
dado un grafo y unas fases iniciales te hace todo el analisis de orden, energia y fases y grafica

mostrar_resultados(G, tiempos, trayectoria, titulo):
es la que hace el grafico (no sabia como hacerlo y que se viera la evolucion de las fases y bueno chat domó)

simulacion(tita0, G)
dado un grafo y fases iniciales es la que resuelve numéricamente el sistema y devuelve un vector de tiempos y un vector de vectores de fases


en grafo_completo.py está el análisis de los grafos completos y muestra que para muchos valores iniciales sincroniza

en grafoo_ciclico.py pueden jugar cambiando el tamaño del grafo (para n<=4 sincroniza globalmente (su conectividad es mayor a 3/4), despúes depende de las condiciones iniciales se puede trabar en los twisted states (2piqj/n))

en grafooo_circulante.py en algun momento estará el analisis de los grafos circulantes donde tambien se traba en los twisted states

en pruebas.py pueden poner cualquier basura, por lo general si queres probar cualquier grafo con condiciones iniciales definis el grafo y las condiciones iniciales corres sincronizar_grafo (quiza la funcion con peor nombre de la historia) y ves si sincronizo o no