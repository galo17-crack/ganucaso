from calentamiento_biblioteca import *

n = 5
G = nx.cycle_graph(n)

tita0 = np.random.uniform(0, 2*np.pi, size=n)
print("Conectividad del grafo:", conectividad(G))
sincronizar_grafo(G, tita0, "Grafo cíclico")
