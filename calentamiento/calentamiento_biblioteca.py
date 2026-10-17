import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

###FUNCIONES AUXILIARES 
def energia(tita, G):
    energia = 0
    for i, j in G.edges():
        energia += (1 - np.cos(tita[i] - tita[j]))
    return energia

def  dvda_tita(tita, G):
    dvda = np.zeros(len(tita))
    for i in range(len(tita)):
        for j in G.neighbors(i):
            dvda[i] += np.sin(tita[j] - tita[i])
    return dvda

def hessiano(tita, G):
    n = len(tita)
    H = np.zeros((n, n))
    for i in range(n):
        for j in G.neighbors(i):
            H[i, i] += np.cos(tita[i] - tita[j])
            H[i, j] -= np.cos(tita[i] - tita[j])
    return H

def conectividad(G):
    mingrado = G.degree(0)
    for i in range(len(G.nodes())):
        if G.degree(i) <= mingrado:
            mingrado = G.degree(i)
    return (1 + mingrado) / len(G.nodes())

def simulacion(tita0, G, T=30, pasos=1000):
    """
    Simula la evolución temporal de un sistema de osciladores acoplados en un grafo G.
    Args: 
        tita0: array de fases iniciales de los osciladores.
        G: grafo que representa la topología de acoplamiento.
        T: tiempo total de simulación.
        pasos: número de pasos de tiempo para la integración.
    Returns:
        t: array de tiempos.
        trayectoria: array de fases de los osciladores a lo largo del tiempo. (traspuesta)
    """
    tiempos = np.linspace(0, T, pasos)
    sol = solve_ivp(lambda t, y: dvda_tita(y, G), [0, T], tita0, t_eval=tiempos)
    return sol.t, sol.y.T

def orden(tita):
    return np.abs(np.mean(np.exp(1j * np.asarray(tita))))

def autoval(tita,G):
    H = hessiano(tita, G)
    autovalores = np.linalg.eigvalsh(H)
    return autovalores

####GRAFICO
def mostrar_resultados(G, tiempos, trayectoria, titulo):
    energias = np.array([energia(x, G) for x in trayectoria])
    N_orden = np.array([orden(x) for x in trayectoria])

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))

    ax[0].plot(tiempos, energias)
    ax[0].set_title("Energía")
    ax[0].set_xlabel("Tiempo")

    ax[1].plot(tiempos, N_orden)
    ax[1].set_title("Parámetro de orden")
    ax[1].set_xlabel("Tiempo")
    ax[1].set_ylim(-0.05, 1.05)

    ax[2].plot(tiempos, np.mod(trayectoria, 2 * np.pi))
    ax[2].set_title("Fases de los osciladores")
    ax[2].set_xlabel("Tiempo")
    ax[2].set_ylabel("Fase (mod. 2π)")

    fig.suptitle(titulo)
    fig.tight_layout()
    plt.show()

def sincronizar_grafo(G, tita0,titulo):
    """
    Función que realiza la simulación de un sistema de osciladores acoplados en un grafo G y muestra los resultados.
    Args:
        G: grafo que representa la topología de acoplamiento.
        tita0: array de fases iniciales de los osciladores.
        titulo: título para los gráficos.
    """
    t, trayectoria = simulacion(tita0, G, T=20)
    tita_final = trayectoria[-1]
    print("Energía inicial:", energia(tita0, G))
    print("Energía final:", energia(tita_final, G))
    print("Parámetro de orden inicial:", orden(tita0))
    print("Parámetro de orden final:", orden(tita_final))
    
    print("Autovalores del Hessiano final:")    
    print(np.round(autoval(tita_final, G), 6))

    mostrar_resultados(G, t, trayectoria, titulo)