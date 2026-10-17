from calentamiento_biblioteca import *

G = nx.erdos_renyi_graph(n=10, p=0.3) #genera un grafo aleatorio
tita0 = np.random.uniform(0, 2*np.pi, size=10) #genera un vector de fases iniciales aleatorias

sincronizar_grafo(G, tita0, "Grafo aleatorio")
