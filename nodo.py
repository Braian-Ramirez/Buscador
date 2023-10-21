class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"<Nodo{self.valor}>"