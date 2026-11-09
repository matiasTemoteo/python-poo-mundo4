
class Numero:

    def __init__(self, valor: int|float = 0):
        self.__valor = valor


    def __str__(self):
        return f'Tenho o valor {self.__valor} dentro do número'


    def dobrar(self):
        self.__valor *= 2


class Texto:

    def __init__(self, txt: str = ""):
        self.__texto = txt


    def __str__(self):
        return f'Tenho o texto "{self.__texto}" dentro do texto'


    def dobrar(self):
        self.__texto += (" " + self.__texto)


class Papel:

    def __init__(self ):
        self.__dobrado = False


    def __str__(self):
        return f'O papel esta Dobrado? -> {"Sim" if self.__dobrado else "Não"}'


    def dobrar(self):
        self.__dobrado = True


class Lista:

    def __init__(self, lst: list = []):
        self.__valores = lst


    def __str__(self):
        return f'Tenho os items {self.__valores} dentro da lista'


    def dobrar(self):
        self.__valores += self.__valores


class Casa:

    def __init__(self):
        pass


    def __str__(self):
        return "Era uma casa muito engraçada..."



# Duck Typing


def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldade para dobrar {objeto.__class__.__name__}")