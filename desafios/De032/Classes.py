from hashlib import sha256


class ContaBancaria:

    def __init__(self, id: int, nome: str = None, saldo: float = 0, chave: str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if chave is None:
            chave = self.pede_senha()

        self.__hash = sha256(chave.encode('utf-8')).hexdigest()

        print(f"Conta {self._id} criada com sucesso. Saldo atual de {self.__saldo:.2f}")


    def pede_senha(self) -> str:

        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha


    def validar_senha(self, chave: str) -> bool:
        usuario = sha256(chave.encode('utf-8')).hexdigest()

        return usuario == self.__hash


    def __str__(self):
        return f"A conta {self._id} do {self._titular} tem R${self.__saldo:.2f} de saldo."


    def depositar(self, valor: float):
        valor = abs(valor)

        if valor > 50000:
            print("O Deposito não pode superar o valor limite de R$50.000,00!")
        else:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:,.2f} autorizado na conta {self._id}")


    def sacar(self, valor: float, chave: str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}, SALDO INSUFICIENTE!")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}!")
        else:
            print(f"Senha não confere, Saque não autorizado!")


    @property
    def nome(self):
        return self._titular


    @nome.setter
    def nome(self, nome: str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(nome) > 5:
                self._titular = nome
            else:
                print("O Novo nome deve ter no mínimo 5 letras!")
        else:
            print("Senha não confere. Não foi possível alterar o nome!")
