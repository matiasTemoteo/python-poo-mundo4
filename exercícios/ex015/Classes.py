
class Carteira:

    def __init__(self, valor: int|float = 0):
        self.__saldo = valor


    def __str__(self):
        return f"Você tem R${self.__saldo:,.2f} na carteira"


    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo dessa maneira!")


    def __eq__(self, outro):
        return self.__saldo == outro.__saldo


    def __iadd__(self, valor: int|float):
        self.__saldo += valor
        return self


    def __sub__(self, valor: int|float):
         self.__saldo -= valor
         return self
