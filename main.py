from fastapi import FastAPI
import mock

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
        words = documento.lower.split()
        for word in words:
            if word in cache:
                cache[word].append(index)
            else:
                cache[word] = [index]
    print(cache)
    return cache.get(palabra["palabra"], "No se encontro")
