from calentamiento_biblioteca import *

n=18
k=4

def grafo_circulante(n, k):
    """
    Genera un grafo circulante con n nodos y k vecinos por lado.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(1, k +1):
            G.add_edge(i, (i + j) % n)
    return G

G = grafo_circulante(n, k)
tita0 =np.random.uniform(0, 2*np.pi, size=n)
sincronizar_grafo(G, tita0, "Grafo circulante")