import re
from abc import ABC, abstractmethod


class Validador(ABC):

    def __init__(self):
        pass


    def check_regular_exp(self, regex_: str, valor: str):
        return re.fullmatch(regex_, valor) is not None


    @abstractmethod
    def validar(self, valor: str):
        pass


class Usuario(Validador):

    def __init__(self):
       super().__init__()


    def validar(self, valor: str):

        return self.check_regular_exp(
            r"^[a-zA-Z0-9_-]{5,20}$",
            valor
        )


class Senha(Validador):

    def __init__(self):
        super().__init__()


    def validar(self, valor: str):

        return self.check_regular_exp(
            r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$",
            valor
        )


class Email(Validador):

    def __init__(self):
        super().__init__()


    def validar(self, valor: str):

        return self.check_regular_exp(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            valor
        )


def validar_dado(validador: Validador, valor: str):

    try:
        is_valid = validador.validar(valor)
        text = f"Valor '{valor}' é valido? -> "
        text += " SIM" if is_valid else " NÃO"
        print(text)
    except:
        print("Não foi possível validar!!")
