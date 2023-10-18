from fastapi import FastAPI
import mock
import json

app = FastAPI()

@app.get("/")
def root():
    return {
        "Servicio": "Estructuras de datos"
    }

@app.post("/indices-invertidos")
def indices_invertidos(palabra: dict):
    cache = {}
    for index, documento in enumerate(mock.my_documento):
        sentences = documento.split()
        for sentence in sentences:
            words = sentence.lower().split()
            for word in words:
                if word in cache:
                    cache[word].append(documento)
                else:
                    cache[word] = [documento]
    return cache.get(palabra["palabra"], "No se encontró")

@app.post("/algoritmo-floyd")
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"<Nodo{self.valor}>"

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

# Crear una lista enlazada con ciclo
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5
nodo5.siguiente = nodo2

# Crear una lista enlazada sin ciclo
nodo1_no_ciclo = Nodo(1)
nodo2_no_ciclo = Nodo(2)
nodo3_no_ciclo = Nodo(3)
nodo4_no_ciclo = Nodo(4)
nodo5_no_ciclo = Nodo(5)

nodo1_no_ciclo.siguiente = nodo2_no_ciclo
nodo2_no_ciclo.siguiente = nodo3_no_ciclo
nodo3_no_ciclo.siguiente = nodo4_no_ciclo
nodo4_no_ciclo.siguiente = nodo5_no_ciclo


def buscar_ciclo(lista):
    liebre = lista
    tortuga = lista

    while liebre and tortuga and liebre.siguiente:
        liebre = liebre.siguiente.siguiente
        tortuga = tortuga.siguiente

        if liebre == tortuga:
            print("Ciclo detectado:", liebre, tortuga)
            return True

    return False

print("Lista con ciclo:")
ciclo_detectado = buscar_ciclo(nodo1)
if not ciclo_detectado:
    print("No se encontró ciclo en la lista.")

print("\nLista sin ciclo:")
ciclo_detectado = buscar_ciclo(nodo1_no_ciclo)
if not ciclo_detectado:
    print("No se encontró ciclo en la lista.\n")

def buscar_numero_repetido(nums):
    numeros_vistos = {}
    resultado = []

    for i, num in enumerate(nums):
        if num in numeros_vistos:
            resultado.append({
                "mensaje": "Se encontró un número repetido.",
                "número_repetido": num,
                "índice_del_número_repetido": [numeros_vistos[num], i]
            })
        numeros_vistos[num] = i

    for res in resultado:
        print(json.dumps(res, ensure_ascii=False))

    if not resultado:
        print(json.dumps({"mensaje": "No se encontró ningún número repetido en la lista."}, ensure_ascii=False))

# Supongamos que tienes una lista de números
numeros = [1, 2, 5, 1, 2, 5, 7, 7]

# Llama a la función para buscar números repetidos en la lista
buscar_numero_repetido(numeros)