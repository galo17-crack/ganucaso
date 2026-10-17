from calentamiento_biblioteca import *


n = 10
G = nx.complete_graph(n)

tita0 = np.random.uniform(0, 2*np.pi, size=n)

sincronizar_grafo(G, tita0, "Grafo completo")

resultados = []
for i in range(100):
    tita0 = np.random.uniform(0, 2*np.pi, size=n)
    t, trayectoria = simulacion(tita0, G, T=20)
    tita_final = trayectoria[-1]
    resultados.append({
        "energia_final": energia(tita_final, G),
        "orden_final": orden(tita_final)
    })

energias = [r["energia_final"] for r in resultados]
ordenes = [r["orden_final"] for r in resultados]
print(energias)
print(ordenes)

print("Orden promedio final:", np.mean(ordenes))
print("Orden mínimo final:", np.min(ordenes))


