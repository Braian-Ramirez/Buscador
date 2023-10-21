from fastapi import FastAPI
import mock
import json

from nodo import Nodo

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
def algoritmo_floyd(nums: dict):
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

    return {
        "resultado": buscar_numero_repetido(nums["numeros"])
    }


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
            return resultado
        numeros_vistos[num] = i

    for res in resultado:
        print(json.dumps(res, ensure_ascii=False))

    if not resultado:
        print(json.dumps({"mensaje": "No se encontró ningún número repetido en la lista."}, ensure_ascii=False))
    return {}
