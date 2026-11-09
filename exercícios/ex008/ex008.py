class ContaBacaria:
    """
    Cria uma conta bancária que permite realizar saques e depósitos
    """

    def __init__(self, id, titular, saldo):
        self.id = id  # publico (+)
        self._titular = titular
        self.__saldo = saldo

    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R$ {self.__saldo:,.2f} de saldo'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R$ {valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque de R$ {valor:,.2f} negado na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:,.2f} autorizado na conta {self.id}")
