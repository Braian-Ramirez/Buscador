from fastapi import FastAPI
import mock
import json
import random
import string
import boto3
from nodo import Nodo

app = FastAPI()
aws_access_key_id = 'AKIAXII2BKO7PPH2CJMQ'
aws_secret_access_key = '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'

sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
queue_url = 'https://sqs.us-east-1.amazonaws.com/498807690174/transacciones_banco'

@app.get("/")
def root():
    # Complejidad: O(1)
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
    # Complejidad: O(n * m), donde n es el número de documentos en `mock.my_documento` y m es el número promedio de palabras en cada documento.
    return cache.get(palabra["palabra"], "No se encontró")
@app.post("/sqs")
def publicar (message: dict):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message['Braian Felipe Ramírez']
    )
    print(f'Mensaje publicado con éxito: {response["MessageId"]}')
    return {
        "id" : response["MessageId"]
    }
@app.get("/sqs")
def procesar ():
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MessageAttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )

    print(response)
    if response.get('Messages'):

        message = response['Messages']

        print(f"Mensaje recibido: {message[0]['ReceiptHandle']}")

        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message[0]['ReceiptHandle']
        )
        return {
             "respuesta": f"mensaje procesado : {message[0]['ReceiptHandle']} "
        }
    else:
        print("No se encontraron mensajes en la cola.")
        return {
            "respuesta":"No se encontraron mensajes en la cola."
        }
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

    # Complejidad: O(1)
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

    # Complejidad: O(n), donde n es el número de elementos en la lista.
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

        # Complejidad: O(n), donde n es el número de elementos en la lista de números.
    return {}


@app.post("/merge-sort")
def generar_documentos():
    # Generar una lista de 500 documentos ordenados alfabéticamente
    documentos = []
    for _ in range(500):
        documento = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        documentos.append(documento)
    documentos.sort()

    # Complejidad: O(1)
    return documentos


# Implementar el algoritmo de Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    # Complejidad: O(n * log(n)), donde n es el número de documentos generados.
    return arr


# Ordenar la lista de documentos utilizando Merge Sort
respuesta = merge_sort(generar_documentos())
print(respuesta)
