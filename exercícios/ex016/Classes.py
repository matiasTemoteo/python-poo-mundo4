



class Pedra:
    def __init__(self):
        pass


# Método Polimorfico Duck Typing


def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir o objeto {objeto.__class__.__name__}")
